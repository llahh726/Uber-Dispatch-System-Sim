from nodes import *
from passengers import *
from uber import *
from util import *

import sys
# a class to hold everything
class Graph:
    # init
    def __init__(self, nodes, passengers, ubers, start_t = 0):
        self.nodes = nodes
        self.passengers = passengers # All the passengers on the map
        self.ubers = ubers
        self.time = start_t # start time
        self.max_time = 10 # time step len
        # just noticed this doesn't support spawning two passengers at the same time
        # self.spawnTimes = [1, 3, 4, 6] # maybe keep a list of times at which to spawn someone
        # commented out/replaced this because I don't want it just yet when I'm testing
        #self.spawnQueue = [Passenger(self.nodes[1], self.nodes[3]), Passenger(self.nodes[2], self.nodes[7]), Passenger(self.nodes[10], self.nodes[1]), Passenger(self.nodes[4], self.nodes[6])] # list of passengers that we want to spawn at above times (arrays must be same len)
        #self.spawnQueue = []
    
    # roads will be two-ways always
    def add_neighbor(self, node1, node2):
        if node1 in node2.neighbors:
            print 'They are already neighbors!'
        else:
            node1.neighbors.append(node2)
            node2.neighbors.append(node1)
    
    # choose a random node to increase its traffic
    # we can delete make t random later
    def ran_traffic(self, t):
        node = np.random.choice(self.nodes)
        node.traffic = t
        print node.node_id
    
    # reset all traffic
    def reset_traffic(self):
        for i in self.nodes:
            i.traffic = 1
    
    # spawn a new passenger with 
    def spawn(self):
        ran_start = np.random.choice(self.nodes)
        tmp_nodes = list(self.nodes)
        tmp_nodes.remove(ran_start)
        ran_dest = np.random.choice(tmp_nodes)
        newPass = Passenger(ran_start, ran_dest)
        self.passengers.append(newPass)


    def pass_time(self):
        for step in range(self.max_time):
            # varyCostOfNodes(self.nodes)

            # we can spawn according to time, or just random
            #if self.time == 5, or ...
                # self.spawn()
            # or just spawn at random with 4/100 chance
            if np.random.randint(0,100) < 4:
                self.spawn()
            for passenger in self.passengers:
                # if arrived, delete
                if passenger.arrived:
                    self.passengers.remove(passenger)

                # ======================== search from passenger's perspective =================================
                if not passenger.got_uber:
                    # print "self.ubers=", self.ubers
                    closestUber = passenger.closestUber_pool(self.ubers)
                    if closestUber:
                        closestUber.assigned_passenger.append(passenger)
                        # see which passenger is closer and go to the closer one
                        if len(closestUber.assigned_passenger) == 1:
                            closestUber.destinationNode = passenger.start
                        elif len(closestUber.assigned_passenger) == 2:
                            passenger1 = closestUber.assigned_passenger[0]
                            passenger2 = closestUber.assigned_passenger[1]
                            came_from1, _ = a_star_search(closestUber.currentNode, passenger1.start)
                            came_from2, _ = a_star_search(closestUber.currentNode, passenger2.start)
                            path1 = reconstruct_path(came_from1, closestUber.currentNode, passenger1.start)
                            path2 = reconstruct_path(came_from2, closestUber.currentNode, passenger2.start)
                            dist1 = get_path_cost(path1)
                            dist2 = get_path_cost(path2)
                            # print "currDist=", currDist
                            if (dist1 <= dist2):
                                closestUber.destinationNode = passenger1.start
                            else:
                                closestUber.destinationNode = passenger2.start
                        else:
                            print 'error here, assigned passenger len not 1 or 2'
                        passenger.got_uber = True
                    # how to we change the dest node later?
                # ======================== search from passenger's perspective =================================

            for uber in self.ubers:
                if uber.destinationNode != None:
                    if uber.currentNode != None:
                        uber.setNodePath()
                    uber.uberMove()
                # ======================== search from uber's perspective =================================
                # else:
                #     closestPass = uber.closestPassenger(self.passengers)
                #     if closestPass:
                #         uber.destinationNode = closestPass.start
                #         uber.assigned_passenger = closestPass
                #         closestPass.got_uber = True
                # ======================== search from uber's perspective =================================


                # check dest for passenger
                # for p in uber.passengers:
                    # if uber.reachedDestination():
                        #uber.passengers.remove(p)
                        #self.passengers.remove(p)
                        #uber.destinationNode = None
                        #uber.passengerCount -= 1
                        # print 'journey done!'
# 

            for p in self.passengers:
                p.time += 1
            # increment self time
            self.time += 1


    # # run spawn and time
    # def pass_time(self):
    #     for step in range(self.max_time):
    #         try:
    #             if step == self.spawnTimes[0]: # spawn and remove from queue
    #                 self.spawn(self.spawnQueue[0])
    #                 del self.spawnQueue[0]
    #                 del self.spawnTimes[0]
    #         except:
    #             pass

    #         # assign unassigned cars to nearest passengers
    #         for uber in self.ubers:
    #             if uber.currentNode != None:
    #                 if uber.passengerCount == 0:
    #                     minDist = sys.maxsize
    #                     assignedTo = False
    #                     for p in self.passengers:
    #                         if (not p.pickedUp): # just look at passengers who need a ride
    #                             currDist = uber.currentNode.get_euc_dist(p.start)
    #                             if (minDist > currDist):
    #                                 print "REACHED CONDITION: New assignment is pass_id:", p.ID
    #                                 minDist = currDist
    #                                 assignedTo = p
    #                     if not assignedTo:
    #                         uber.pickupPassenger(assignedTo)
    #                         print "ASSIGNED Uber", uber.carId, "to", assignedTo.ID
    #                         assignedTo.pickedUp = True
    #                     else:
    #                         print "No one was assigned! (Could mean everyone has been picked up)"
    #                         #print "self.passengers is", self.passengers
    #                         #for p in self.passengers:
    #                         #    print "status is", p.pickedUp
    #                         #print ">>>"
    #                 else:
    #                     # check for arrivals and kill passengers who are done
    #                     print "Check if reached destination"
    #                     for uber in self.ubers:
    #                         retval = uber.reachedDestination()
    #                         if retval >= 0:
    #                             del self.passengers[retval]
    #                 if len(uber.nodePath) == 0:
    #                     uber.setNodePath()
    #                 try:
    #                     uber.uberMove(uber.nodePath[0]) # get next node from the route returned by search alg  
    #                     del uber.nodePath[0]
    #                 except:
    #                     print "nodePath[] empty"

    #         for p in self.passengers: # increment their time in the system
    #             p.time += 1

    # euclidian 
    def euclidian_heuristic(self, node1, node2):
        a = np.array([node1.x, node1.y])
        b = np.array([node2.x, node2.y])
        return np.sqrt(np.sum((a-b)**2))
    
    # a star search for finding a best route
    def a_star_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = collections.OrderedDict()
        cost_so_far = collections.OrderedDict()
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for neighbor in current.get_neighbors():
                # cost = current cost + dist + current traffic + neighbor traffic
                new_cost = cost_so_far[current] + current.get_euc_dist(neighbor) + current.traffic + neighbor.traffic
                # a star
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.euclidian_heuristic(goal, neighbor)
                    frontier.put(neighbor, priority)
                    came_from[neighbor] = current

        return came_from, cost_so_far

    # DFS / BFS, method -> 'DFS', 'BFS'
    def depth_breadth_first_search(self, method, start, goal):
        if method == 'BFS':
            frontier = Queue()
        elif method == 'DFS':
            frontier = Stack()
        else:
            print 'method invalid'
        # init frontier
        frontier.put(start)
        came_from = collections.OrderedDict()
        came_from[start] = None
        
        # run search
        while not frontier.empty():
            current = frontier.get()
            
            if current == goal:
                break
            
            for neighbor in current.get_neighbors():
                if neighbor not in came_from:
                    frontier.put(neighbor)
                    came_from[neighbor] = current
        
        return came_from

    # some tiny modification from A star
    def uniform_cost_search(self, start, goal):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = collections.OrderedDict()
        cost_so_far = collections.OrderedDict()
        came_from[start] = None
        cost_so_far[start] = 0
        
        while not frontier.empty():
            current = frontier.get()
            
            if current == goal:
                break
            
            for neighbor in current.get_neighbors():
                new_cost = cost_so_far[current] + current.get_euc_dist(neighbor) + current.traffic + neighbor.traffic
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost
                    frontier.put(neighbor, priority)
                    came_from[neighbor] = current
        
        return came_from, cost_so_far


    # a helper function to get the path
    # return path from start to final in a list of nodes
    def reconstruct_path(self, came_from, start, goal):
        current = goal
        path = [current]
        while current != start:
            current = came_from[current]
            path.append(current)
        path.reverse() 
        return path


    # pass it path from the above function, it will return the cost of the path
    def get_path_cost(self, path):
        cursor = 1
        cost = 0
        while cursor != len(path):
            cost += path[cursor-1].get_euc_dist(path[cursor]) + path[cursor-1].traffic + path[cursor].traffic
            cursor += 1
        return cost



if __name__ == '__main__':


    n1 = Node(x=0, y=0, neighbors=[], passengers=[])
    n2 = Node(x=50, y=0, neighbors=[], passengers=[])
    n3 = Node(x=100, y=0, neighbors=[], passengers=[])
    n4 = Node(x=0, y=50, neighbors=[], passengers=[])
    n5 = Node(x=50, y=50, neighbors=[], passengers=[])
    n6 = Node(x=100, y=50, neighbors=[], passengers=[])
    n7 = Node(x=0, y=100, neighbors=[], passengers=[])
    n8 = Node(x=50, y=100, neighbors=[], passengers=[])
    n9 = Node(x=100, y=100, neighbors=[], passengers=[])
    n10 = Node(x=25, y=25, neighbors=[], passengers=[])
    n11 = Node(x=25, y=75, neighbors=[], passengers=[])
    n12 = Node(x=75, y=25, neighbors=[], passengers=[])
    n13 = Node(x=75, y=75, neighbors=[], passengers=[])
    n14 = Node(x=10, y=10, neighbors=[], passengers=[])
    n15 = Node(x=90, y=90, neighbors=[], passengers=[])
    n16 = Node(x=10, y=90, neighbors=[], passengers=[])
    n17 = Node(x=90, y=10, neighbors=[], passengers=[])
    n18 = Node(x=25, y=60, neighbors=[], passengers=[])
    n19 = Node(x=40, y=25, neighbors=[], passengers=[])
    n20 = Node(x=75, y=40, neighbors=[], passengers=[])
    n21 = Node(x=60, y=75, neighbors=[], passengers=[])
    add_neighbor(n1, n2)
    add_neighbor(n2, n3)
    add_neighbor(n1, n4)
    add_neighbor(n2, n5)
    add_neighbor(n3, n6)
    add_neighbor(n4, n7)
    add_neighbor(n5, n8)
    add_neighbor(n6, n9)
    add_neighbor(n4, n5)
    add_neighbor(n5, n6)
    add_neighbor(n7, n8)
    add_neighbor(n8, n9)
    add_neighbor(n1, n14)
    add_neighbor(n14, n10)
    add_neighbor(n10, n5)
    add_neighbor(n4, n10)
    add_neighbor(n10, n2)
    add_neighbor(n5, n12)
    add_neighbor(n12, n17)
    add_neighbor(n17, n3)
    add_neighbor(n2, n12)
    add_neighbor(n12, n6)
    add_neighbor(n4, n11)
    add_neighbor(n11, n8)
    add_neighbor(n7, n16)
    add_neighbor(n16, n11)
    add_neighbor(n11, n5)
    add_neighbor(n5, n13)
    add_neighbor(n13, n15)
    add_neighbor(n15, n9)
    add_neighbor(n8, n13)
    add_neighbor(n13, n6)

    add_neighbor(n11, n18)
    add_neighbor(n10, n19)
    add_neighbor(n12, n20)
    add_neighbor(n13, n21)
    nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17, n18, n19, n20, n21]

    # p1 = Passenger(n1, n2)
    # p2 = Passenger(n10, n12)
    # p3 = Passenger(n5, n14)
    # p4 = Passenger(n11, n1)
    # p5 = Passenger(n4, n9)
    # passengers = [p1, p2, p3, p4 ,p5]


    # # self, carId, passengerCount, passengers, x, y, nodePath, currentNode, destinationNode, currentTotalTravelCost

    u1 = Uber(0, [], n1.x, n1.y, [], n1,  None, 0, [])
    u2 = Uber(0, [], n7.x, n7.y, [],n7,  None, 0, [])
    u3 = Uber(0, [], n9.x, n9.y, [], n9, None, 0, [])
    u4 = Uber(0, [], n11.x, n11.y, [], n11,  None, 0, [])
    u5 = Uber(0, [], n15.x, n15.y, [], n15,  None, 0, [])
    u6 = Uber(0, [], n15.x, n15.y,  [], n15, None, 0, [])

    # ubers = [u1, u2, u3, u4, u5, u6]
    ubers = [u1, u2, u3, u4, u5]


    # g = Graph(nodes=nodes, passengers=passengers, ubers=ubers)

    

    # Ubers
    #u1 = Uber(carId=1, passengerCount=0, passengers=[], x=0, y=0, nodePath=[], currentNode=n1, destinationNode=None, currentTotalTravelCost=0, assigned_passenger = None)
    #2 = Uber(2, 0, [], 100, 100, [], n9, None, 0,None)
    #u3 = Uber(3, 0, [], 100, 0, [], n14, None, 0)
    # ubers = [u1, u2]
    # Passengers

    p1 = Passenger(n3, n7)

    p2 = Passenger(n1, n10)
    p3 = Passenger(n11, n1)
    p4 = Passenger(n15, n4)
    p5 = Passenger(n7, n2)

    # passengerList = [p1, p2, p3 ,p4 ,p5]
    passengerList = [p1, p2, p3, p4, p5]
    # passengerList = [p1, p2]

    g = Graph(nodes=nodes, passengers=passengerList, ubers=ubers)

    # graph it
    

    #print "Uber1 pos:", u1.currentNode.x, u1.currentNode.y
    #print "Uber2 pos:", u2.currentNode.x, u2.currentNode.y
    #print "Uber3 pos:", u3.currentNode.x, u3.currentNode.y

    # print passengerList
    # print "Passengers", g.passengers

    # tuple = g.a_star_search(n10, n6)
    # path = tuple[0]
    # cost = tuple[1]
    # print "Path:", path.items()[0][0]
    # for x in path:
    #     print x.node_id, x.x, x.y
    # print cost
    # #for x in cost:
    # print x.node_id

    # Get cost at each step
    # for i in cost:
    #     print cost[i]
    #print "Path:", path(1)

    # nodePathList = nodePathToList(path)


    for i in range(40):
        print graph_map(g)

        g.pass_time()
    # ubers = g.ubers
    # for u in ubers:
    #     print u.carId
    # passengers = g.passengers
    # for p in passengers:
    #     print p.ID
    # for u in ubers:
    #     path = u.nodePath
    #     for p in path:
    #         print p.x, p.y
        #print u.currentNode.x, u.currentNode.y
        # print u.destinationNode.x, u.destinationNode.y
        # print u.currentTotalTravelCost
        # print u.passengers

    print graph_map(g)

