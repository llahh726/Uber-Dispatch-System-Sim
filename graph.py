from nodes import *
from passengers import *
from uber import *
from util import *

import sys


PAS_ID = 0

# a class to hold everything
class Graph:
    # init
    def __init__(self, nodes, passengers, ubers, start_t = 0):
        self.nodes = nodes
        self.passengers = passengers # All the passengers on the map
        self.ubers = ubers
        self.time = start_t # start time
        self.max_time = 10 
        # just noticed this doesn't support spawning two passengers at the same time
        self.spawnTimes = [1, 3, 4, 6] # maybe keep a list of times at which to spawn someone
        # commented out/replaced this because I don't want it just yet when I'm testing
        #self.spawnQueue = [Passenger(self.nodes[1], self.nodes[3]), Passenger(self.nodes[2], self.nodes[7]), Passenger(self.nodes[10], self.nodes[1]), Passenger(self.nodes[4], self.nodes[6])] # list of passengers that we want to spawn at above times (arrays must be same len)
        self.spawnQueue = []
    
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
    
    # spawn new passengers
    def spawn(self, newPass):
        global PAS_ID
        newPass.ID = PAS_ID # set the correct ID to new passenger
        self.passengers.append(newPass)
        PAS_ID += 1

        # for p in passengers:
        #    print p.info()

    # run spawn and time
    def pass_time(self):
        for step in range(self.max_time):
            try:
                if step == self.spawnTimes[0]: # spawn and remove from queue
                    self.spawn(self.spawnQueue[0])
                    del self.spawnQueue[0]
                    del self.spawnTimes[0]
            except:
                pass

            # assign unassigned cars to nearest passengers
            for uber in self.ubers:
                if uber.passengerCount == 0:
                    minDist = sys.maxsize
                    assignedTo = None # not sure if this is a proper initialization
                    for p in self.passengers:
                        if (not p.pickedUp): # just look at passengers who need a ride
                            currDist = uber.currentNode.get_euc_dist(p.start)
                            if (minDist > currDist):
                                print "REACHED CONDITION"
                                minDist = currDist
                                assignedTo = p
                    if assignedTo != None:
                        uber.pickupPassenger(assignedTo)
                        assignedTo.pickedUp = True
                    else:
                        print "self.passengers is", self.passengers
                        for p in self.passengers:
                            print "status is", p.pickedUp
                        print ">>>"
                else:
                    # uber.reachedDestination()
                    print "Check if reached destination"


            for p in self.passengers: # increment their time in the system
                p.time += 1
                
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
                new_cost = cost_so_far[current] + current.get_euc_dist(neighbor) * current.traffic + neighbor.traffic
                # a star
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.euclidian_heuristic(goal, neighbor)
                    frontier.put(neighbor, priority)
                    came_from[neighbor] = current

        return came_from, cost_so_far

    # DFS / BFS, method -> 'DFS', 'BFS'
    def depth_breadth_first_search(method, start, goal):
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


    



if __name__ == '__main__':

    # test for graph
    n1 = Node(node_id=NODE_ID, x=0, y=0, neighbors=[], passengers=[])
    n2 = Node(node_id=NODE_ID, x=50, y=0, neighbors=[], passengers=[])
    n3 = Node(node_id=NODE_ID, x=100, y=0, neighbors=[], passengers=[])
    n4 = Node(node_id=NODE_ID, x=0, y=50, neighbors=[], passengers=[])
    n5 = Node(node_id=NODE_ID, x=50, y=50, neighbors=[], passengers=[])
    n6 = Node(node_id=NODE_ID, x=100, y=50, neighbors=[], passengers=[])
    n7 = Node(node_id=NODE_ID, x=0, y=100, neighbors=[], passengers=[])
    n8 = Node(node_id=NODE_ID, x=50, y=100, neighbors=[], passengers=[])
    n9 = Node(node_id=NODE_ID, x=100, y=100, neighbors=[], passengers=[])
    n10 = Node(node_id=NODE_ID, x=25, y=25, neighbors=[], passengers=[])
    n11 = Node(node_id=NODE_ID, x=25, y=75, neighbors=[], passengers=[])
    n12 = Node(node_id=NODE_ID, x=75, y=25, neighbors=[], passengers=[])
    n13 = Node(node_id=NODE_ID, x=75, y=75, neighbors=[], passengers=[])
    n14 = Node(node_id=NODE_ID, x=10, y=10, neighbors=[], passengers=[])
    n15 = Node(node_id=NODE_ID, x=90, y=90, neighbors=[], passengers=[])
    n16 = Node(node_id=NODE_ID, x=10, y=90, neighbors=[], passengers=[])
    n17 = Node(node_id=NODE_ID, x=90, y=10, neighbors=[], passengers=[])

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
    nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16, n17]
    g = graph(nodes=nodes, passengers=[], ubers=[])

    # graph it
    print graph_map(g)

    # Ubers
    u1 = Uber(1, 0, [], n1, None, 0)
    u2 = Uber(2, 0, [], n9, None, 0)
    u3 = Uber(3, 0, [], n14, None, 0)
    ubers = [u1, u2, u3]
    # Passengers
    p1 = Passenger(n3, n7, 1)
    p2 = Passenger(n1, n10, 2)
    p3 = Passenger(n11, n4, 3)
    p4 = Passenger(n15, n4, 4)
    p5 = Passenger(n7, n2, 5)
    passengerList = [p1, p2, p3, p4, p5]

    g = Graph(nodes=nodes, passengers=passengerList, ubers=ubers)

    print "Uber1 pos:", u1.currentNode.x, u1.currentNode.y
    print "Uber2 pos:", u2.currentNode.x, u2.currentNode.y
    print "Uber3 pos:", u3.currentNode.x, u3.currentNode.y
    # passengerList = passengers.spawn(5, nodes)
    print passengerList
    # print passengerList
    # g.passengers = passengerList
    # print "Passengers", g.passengers

    tuple = g.a_star_search(n10, n6)
    path = tuple[0]
    cost = tuple[1]
    # for x in path:
    #     print x.node_id, x.x, x.y
    #     print x
    # print cost
    # #for x in cost:
    # print x.node_id

    # Get cost at each step
    # for i in cost:
    #     print cost[i]

