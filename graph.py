
'''
    CS182 Final Project
    Ying-ke Chin-Lee, Chris Rodowicz, and Jiacheng Zhao
'''
from util import *

import sys
allPassengers = []
pool = False # or False :P
# a class to hold everything
class Graph:
    # init
    def __init__(self, nodes, passengers, ubers, start_t = 0):
        self.nodes = nodes
        self.passengers = passengers # All the passengers on the map
        self.ubers = ubers
        self.time = start_t # start time
        self.max_time = 30 # time step len
    
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
        allPassengers.append(newPass)

    def pass_time(self):
        varyCostOfNodes(self.nodes)
        for step in range(self.max_time):

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
                    if pool: closestUber = passenger.closestUber_pool(self.ubers)
                    else: closestUber = passenger.closestUber(self.ubers)
                    if closestUber:
                        closestUber.assigned_passenger.append(passenger)
                        # see which passenger is closer and go to the closer one
                        if len(closestUber.assigned_passenger) == 1:
                            closestUber.destinationNode = passenger.start
                        elif len(closestUber.assigned_passenger) == 2:
                            passenger1 = closestUber.assigned_passenger[0]
                            passenger2 = closestUber.assigned_passenger[1]
                            came_from1, _ = a_star_search(closestUber.currentNode, passenger1.start, True)
                            came_from2, _ = a_star_search(closestUber.currentNode, passenger2.start, True)
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


    # # self, carId, passengerCount, passengers, x, y, nodePath, currentNode, destinationNode, currentTotalTravelCost

    u1 = Uber(0, [], n1.x, n1.y, [], n1,  None, 0, [])
    u2 = Uber(0, [], n7.x, n7.y, [],n7,  None, 0, [])
    u3 = Uber(0, [], n9.x, n9.y, [], n9, None, 0, [])
    u4 = Uber(0, [], n11.x, n11.y, [], n11,  None, 0, [])
    u5 = Uber(0, [], n15.x, n15.y, [], n15,  None, 0, [])
    u6 = Uber(0, [], n15.x, n15.y,  [], n15, None, 0, [])

    # ubers = [u1, u2, u3, u4, u5, u6]
    ubers = [u1, u2, u3, u4, u5]



    p1 = Passenger(n3, n7)

    p2 = Passenger(n1, n10)
    p3 = Passenger(n11, n1)
    p4 = Passenger(n15, n4)
    p5 = Passenger(n7, n2)

    # passengerList = [p1, p2, p3 ,p4 ,p5]
    passengerList = [p1, p2, p3, p4, p5]
    # passengerList = [p1, p2]

    # our set, beautiful default map
    g1 = Graph(nodes=nodes, passengers=passengerList, ubers=ubers)

    # a random map for testing larger number of nodes
    ran_nodes = gen_random_nodes(100)
    ran_pass = gen_random_passengers(ran_nodes, 10)
    ran_uber = gen_random_ubers(ran_nodes, 6)
    g2 = Graph(nodes=ran_nodes, passengers=ran_pass, ubers=ran_uber)

    # # run function for g1
    for i in range(20):
        print graph_map(g1)
        g1.pass_time()

    # run function for g2
    # the number is the number of time steps!
    # for i in range(20):
    #     print graph_map(g2)
    #     g2.pass_time()


