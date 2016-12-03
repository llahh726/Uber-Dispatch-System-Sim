import nodes
import passengers
import uber
PAS_ID = 0

# a class to hold everything
class graph:
    # init
    def __init__(self, nodes, passengers, ubers, start_t = 0):
        self.nodes = nodes
        self.passengers = passengers
        self.ubders = ubers
        self.time = start_t # start time
        self.max_time = 10 
        self.spawnTimes = [1, 3, 4] # maybe keep a list of times at which to spawn someone
        self.spawnQueue = ['a','b','c'] # list of passengers that we want to spawn at above times (arrays must be same len)
    
    # roads will be two-ways always
    def add_neighbor(self, node1, node2):
        if node1 in node2.neighbors:
            print 'They are already neighrbors!'
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
    def spawn(self):
        global PAS_ID
        # work in progress: where do I get the coordinates?
        passengers = []
        # so nodes would actually have to be made first
        for i in xrange(n):
            passengers.append(Passenger(random.choice(nodes), random.choice(nodes), ID_INDEX))
            PAS_ID += 1

        for p in passengers:
            print p.info()

    # run spawn and time
    def pass_time(self):
        for step in range(self.max_time):
            if step == self.spawnTimes[0]: # spawn and remove from queue
                self.spawn(self.spawnQueue[0])
                del self.spawnQueue[0]
                del self.spawnTimes[0]
            # assign unassigned cars to nearest passengers
            for uber in self.ubers:
                if uber.passengerCount == 0:
                    minDist = sys.maxsize
                    assignedTo = None # not sure if this is a proper initialization
                    for p in passengers:
                        if (not p.pickedUp): # just look at passengers who need a ride
                            currDist = get_euc_dist(car.currentNode, p.start)
                            if (minDist > currDist):
                                minDist = currDist
                                assignedTo = p
                    car.pickupPassenger(assignedTo)
                    assignedTo.pickedUp = True

            for p in passengers: # increment their time in the system
                p.time += 1



if __name__ == '__main__':
    n1 = Node(node_id=NODE_ID, x=1, y=1, neighbors=[], passengers=[])
    n2 = Node(node_id=NODE_ID, x=2, y=3, neighbors=[], passengers=[])
    n3 = Node(node_id=NODE_ID, x=3, y=4, neighbors=[], passengers=[])
    n4 = Node(node_id=NODE_ID, x=10, y=1, neighbors=[], passengers=[])
    n5 = Node(node_id=NODE_ID, x=15, y=30, neighbors=[], passengers=[])
    n6 = Node(node_id=NODE_ID, x=35, y=4, neighbors=[], passengers=[])
    n7 = Node(node_id=NODE_ID, x=89, y=11, neighbors=[], passengers=[])
    n8 = Node(node_id=NODE_ID, x=15, y=35, neighbors=[], passengers=[])
    n9 = Node(node_id=NODE_ID, x=40, y=44, neighbors=[], passengers=[])
    n10 = Node(node_id=NODE_ID, x=10, y=91, neighbors=[], passengers=[])
    n11 = Node(node_id=NODE_ID, x=55, y=87, neighbors=[], passengers=[])
    n12 = Node(node_id=NODE_ID, x=99, y=99, neighbors=[], passengers=[])
    n13 = Node(node_id=NODE_ID, x=15, y=10, neighbors=[], passengers=[])
    n14 = Node(node_id=NODE_ID, x=86, y=30, neighbors=[], passengers=[])
    n15 = Node(node_id=NODE_ID, x=36, y=59, neighbors=[], passengers=[])
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
    g = graph(nodes=nodes, passengers=[], ubers=[])