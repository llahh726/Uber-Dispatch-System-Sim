# all util helper class and functions 
import collections
import heapq
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

NODE_ITERATOR = 0

class Stack:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.pop()

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

def graph_map(graph):
    # init
    xs, ys, ids, edges = [], [], [], []
    # get values we need
    for i in graph.nodes:
        xs.append(i.x)
        ys.append(i.y)
        ids.append(i.node_id)
        for n in i.neighbors:
            edges.append([i.x, n.x, i.y, n.y])
    
    # make format into np so we can graph easily
    xs = np.array(xs)
    ys = np.array(ys)
    ids = np.array(ids)

    # graph the map
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    # main graph
    ax = plt.scatter(xs, ys, marker='o', alpha = 0.7, color = 'g')
    # labels
    for label, x, y in zip(ids, xs, ys):
        plt.annotate(
            label, 
            xy = (x, y), xytext = (-10, 10),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.3', fc = 'blue', alpha = 0.1),
            arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))

    # plot edges
    for edge in edges:
        plt.plot(edge[:2], edge[2:], '-', color = 'blue', alpha = 0.3)
    plt.show()

def nodePathToList(path):
        nodePathList = []
        for i in path:
            nodePathList.append(i)
        return nodePathList

def getNextNodeInPath(nodePathList):
    #print "Node in path:", NODE_ITERATOR, path[NODE_ITERATOR]
    global NODE_ITERATOR
    index = NODE_ITERATOR
    NODE_ITERATOR += 1
    return nodePathList[index]

# Jason:
# maybe a better traffic varying function (not that important now)
# write DFS, BFS, UCF for difference viewing
# think about what the poster what look like 
