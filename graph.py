import nodes
import passengers
import uber
import util

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
        self.spawnTimes = [1, 3, 4] # maybe keep a list of times at which to spawn someone
        self.spawnQueue = ['a','b','c'] # list of passengers that we want to spawn at above times (arrays must be same len)
    
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
        self.passengers.append(newPass)

        # for p in passengers:
        #    print p.info()

    # run spawn and time
    def pass_time(self):
        global PAS_ID
        for step in range(self.max_time):
            if step == self.spawnTimes[0]: # spawn and remove from queue
                self.spawn(self.spawnQueue[0])
                PAS_ID += 1
                del self.spawnQueue[0]
                del self.spawnTimes[0]
            # assign unassigned cars to nearest passengers
            for uber in self.ubers:
                if uber.passengerCount == 0:
                    minDist = sys.maxsize
                    assignedTo = None # not sure if this is a proper initialization
                    for p in self.passengers:
                        if (not p.pickedUp): # just look at passengers who need a ride
                            currDist = get_euc_dist(car.currentNode, p.start)
                            if (minDist > currDist):
                                minDist = currDist
                                assignedTo = p
                    car.pickupPassenger(assignedTo)
                    assignedTo.pickedUp = True
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
    
    # a star search for finding a 
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



if __name__ == '__main__':
    # Nodes
    n1 = Node(node_id=NODE_ID, x=1, y=1, neighbors=[], passengers=[], traffic=1)
    n2 = Node(node_id=NODE_ID, x=2, y=3, neighbors=[], passengers=[], traffic=1)
    n3 = Node(node_id=NODE_ID, x=3, y=4, neighbors=[], passengers=[], traffic=1)
    n4 = Node(node_id=NODE_ID, x=10, y=1, neighbors=[], passengers=[], traffic=1)
    n5 = Node(node_id=NODE_ID, x=15, y=30, neighbors=[], passengers=[], traffic=1)
    n6 = Node(node_id=NODE_ID, x=35, y=4, neighbors=[], passengers=[], traffic=1)
    n7 = Node(node_id=NODE_ID, x=89, y=11, neighbors=[], passengers=[], traffic=1)
    n8 = Node(node_id=NODE_ID, x=15, y=35, neighbors=[], passengers=[], traffic=1)
    n9 = Node(node_id=NODE_ID, x=40, y=44, neighbors=[], passengers=[], traffic=1)
    n10 = Node(node_id=NODE_ID, x=10, y=91, neighbors=[], passengers=[], traffic=1)
    n11 = Node(node_id=NODE_ID, x=55, y=87, neighbors=[], passengers=[], traffic=1)
    n12 = Node(node_id=NODE_ID, x=99, y=99, neighbors=[], passengers=[], traffic=1)
    n13 = Node(node_id=NODE_ID, x=15, y=10, neighbors=[], passengers=[], traffic=1)
    n14 = Node(node_id=NODE_ID, x=86, y=30, neighbors=[], passengers=[], traffic=1)
    n15 = Node(node_id=NODE_ID, x=36, y=59, neighbors=[], passengers=[], traffic=1)
    
    # Connections
    add_neighbor(n1, n2)
    add_neighbor(n2, n3)
    add_neighbor(n3, n4)
    add_neighbor(n1, n4)
    add_neighbor(n4, n5)
    add_neighbor(n3, n6)
    add_neighbor(n6, n7)
    add_neighbor(n5, n8)
    add_neighbor(n8, n9)
    add_neighbor(n9, n10)
    add_neighbor(n10, n11)
    add_neighbor(n11, n12)
    add_neighbor(n12, n13)
    add_neighbor(n14, n13)
    add_neighbor(n15, n14)
    nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]

    # Ubers
    u1 = Uber(UBER_ID, 0, [], n1, None, 0)
    u2 = Uber(UBER_ID, 0, [], n9, None, 0)
    u3 = Uber(UBER_ID, 0, [], n14, None, 0)
    ubers = [u1, u2, u3]
    # Passengers
    p1 = Passenger(n3, n7, ID_INDEX)
    p2 = Passenger(n1, n10, ID_INDEX)
    p3 = Passenger(n11, n4, ID_INDEX)
    p4 = Passenger(n15, n4, ID_INDEX)
    p5 = Passenger(n7, n2, ID_INDEX)
    passengerList = [p1, p2, p3, p4, p5]

    g = graph(nodes=nodes, passengers=passengerList, ubers=ubers)


    # passengerList = passengers.spawn(5, nodes)
    # print passengerList
    # g.passengers = passengerList
    # print "Passengers", g.passengers


