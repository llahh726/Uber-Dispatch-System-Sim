'''
    CS182 Final Project
    Ying-ke Chin-Lee, Chris Rodowicz, and Jiacheng Zhao
'''
import numpy as np
import passengers

class Node:
    # init values
    NODE_ID = 0
    def __init__(self, neighbors, passengers, x=0, y=0, traffic=1):
        self.node_id = Node.NODE_ID
        self.x = x
        self.y = y
        self.traffic = traffic
        self.neighbors = neighbors
        self.passengers = passengers
        Node.NODE_ID += 1
    
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

    
