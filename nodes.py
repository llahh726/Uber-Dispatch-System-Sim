'''
Names...

CS 182 Final Project

Node class for Uber Dispatch System

Node -> intersection of rodes
'''
import numpy as np
import passengers
NODE_ID = 0

class Node:
    # init values
    def __init__(self, node_id, neighbors, passengers, x=0, y=0, traffic=1):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.traffic = traffic
        self.neighbors = neighbors
        self.passengers = passengers
        global NODE_ID
        NODE_ID += 1
    
    # return neighbors
    def get_neighbors(self):
        return self.neighbors
    
    # coordinates
    def get_coord(self):
        return (self.x, self.y)
    
    # get passengers
    def get_passengers(self):         
        return self.passengers
    
    # remove passengers (for pick up)
    def remove_passenger(self, passenger):
        if passenger not in self.passengers:
            print 'Error: passenger not found'
        else:
            self.passengers.remove(passenger)
    
    # add passengers
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    # get traffic
    def get_traffic(self):
        return self.traffic
    
    # update traffic
    def update_traffic(self, traf):
        self.traffic = traf
       
    # get Euclidean dist between two nodes
    # when using this, don't forget to take into account traffic
    def get_euc_dist(self, node):
        a = np.array([self.x, self.y])
        b = np.array([node.x, node.y])
        return np.sqrt(np.sum((a-b)**2))

        

# if __name__ == '__main__':
#     aa = Node(node_id=10)
#     bb = Node(node_id=11, x=12, y=50)
#     cc = Node(node_id=12, x=111, y=3)
#     add_neighbor(aa, bb)
#     for i in aa.neighbors:
#         print i.node_id
#     for i in cc.neighbors:
#         print i.node_id
#     print aa.get_euc_dist(cc)
#     aa.add_passenger('a')
#     print 'aa passengers: ', aa.passenters
#     print 'bb passengers: ', bb.passenters
#     print 'cc passengers: ', cc.passenters

