'''
Names...

CS 182 Final Project

Node class for Uber Dispatch System

Node -> intersection of rodes
'''
class Node(object):
    # init values
    def __init__(self, node_id, x=0, y=0, traffic=1, neighbors=set(), passengers=[]):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.traffic = traffic
        self.neighbors = neighbors
        self.passengers = passengers
    
    # return neighbors
    def get_neighbors(self):
        return self.neighbors
    
    # add neighbors (doesn't have to be mutual, could be one way)
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.add(neighbor)
    
    # coordinates
    def get_coord(self):
        return (self.x, self.y)
    
    # get passengers
    def get_passengers(self):
        return self.passengers
    
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
    

		
