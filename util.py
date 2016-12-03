# all util helper class and functions 
import collections
import heapq

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# no one-ways! roads will be two-ways always
# use this to add node or use 
def add_neighbor(node1, node2):
    if node1 in node2.neighbors:
        print 'They are already neighrbors!'
    else:
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)