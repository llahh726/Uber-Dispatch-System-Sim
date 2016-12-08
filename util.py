# all util helper class and functions 
import collections
import heapq
import random
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
    # init for nodes
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
    ax = plt.scatter(xs, ys, marker='o', alpha = 0.4, s = 100, color = 'g', label='Locations')
    # labels
    for label, x, y in zip(ids, xs, ys):
        plt.annotate(
            label, 
            xy = (x, y), xytext = (-10, 10),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.3', fc = 'green', alpha = 0.1),
            arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))

    # plot edges
    for edge in edges:
        plt.plot(edge[:2], edge[2:], '-', color = 'blue', alpha = 0.3)   
    
    # print ubers that don't have passengers
    uxs1 = []
    uys1 = []
    uids1 = []
    uxs2 = []
    uys2 = []
    uids2 = []
    for u in graph.ubers:
        if not u.passengers:
            uxs1.append(u.x)
            uys1.append(u.y)
            uids1.append(u.carId)
        else:
            uxs2.append(u.x)
            uys2.append(u.y)
            uids2.append(u.carId)
    # plot again
    ax = plt.scatter(uxs1, uys1, marker='s', alpha = 0.6, s = 50, color = 'red', label='Ubers without Passengers')
    ax = plt.scatter(uxs2, uys2, marker='D', alpha = 0.6, s = 50, color = 'crimson', label='Ubers with Passengers')
    # labels
    for label, x, y in zip(uids1, uxs1, uys1):
        plt.annotate(
            label, 
            xy = (x, y), xytext = (20, 20),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.2', fc = 'red', alpha = 0.1),
            arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))
    # labels
    for label, x, y in zip(uids2, uxs2, uys2):
        plt.annotate(
            label, 
            xy = (x, y), xytext = (20, 20),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.2', fc = 'orange', alpha = 0.1),
            arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))
        
    # now graph passengers
    pxs = []
    pys = []
    pids = []
    for p in graph.passengers:
        if p.pickedUp == False:
            pxs.append(p.start.x)
            pys.append(p.start.y)
            pids.append(p.ID)
    # plot again
    ax = plt.scatter(pxs, pys, marker='^', alpha = 0.9, s = 25, color = 'b', label='Passengers')
    # labels
    for label, x, y in zip(pids, pxs, pys):
        plt.annotate(
            label, 
            xy = (x, y), xytext = (15, -15),
            textcoords = 'offset points', ha = 'right', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.1', fc = 'blue', alpha = 0.1),
            arrowprops = dict(arrowstyle = '-', connectionstyle = 'arc3,rad=0'))
    
    plt.legend(bbox_to_anchor=(0, 0), loc=2, borderaxespad=0.)    
    plt.show(block=False)



def getNextNodeInPath(nodePathList):
    #print "Node in path:", NODE_ITERATOR, path[NODE_ITERATOR]
    global NODE_ITERATOR
    index = NODE_ITERATOR
    NODE_ITERATOR += 1
    return nodePathList[index]

# euclidian 
def euclidian_heuristic(node1, node2):
    a = np.array([node1.x, node1.y])
    b = np.array([node2.x, node2.y])
    return np.sqrt(np.sum((a-b)**2))

# a star search for finding a best route
def a_star_search(start, goal, traffic = False):
    # print "Start", start
    # print "Goal", goal
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
            new_cost = cost_so_far[current] + current.get_euc_dist(neighbor) 
            # a star
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                # print "Goal:", goal
                # print "Neighbor:", neighbor
                if traffic:
                    priority = new_cost + euclidian_heuristic(goal, neighbor)*neighbor.traffic
                else:
                    priority = new_cost + euclidian_heuristic(goal, neighbor)
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

# some tiny modification from A star
def uniform_cost_search(start, goal):
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
def reconstruct_path(came_from, start, goal):
    #print "Camefrom", came_from
    #print "Start", start
    #print "Goal", goal
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse() 
    return path


# pass it path from the above function, it will return the cost of the path
def get_path_cost(path):
    cursor = 1
    cost = 0
    while cursor != len(path):
        cost += path[cursor-1].get_euc_dist(path[cursor]) + path[cursor-1].traffic + path[cursor].traffic
        cursor += 1
    return cost

# passed list of all nodes in graph
# function called at every time step
# Higher node.traffic means more traffic and cars wont move as much per turn
def varyCostOfNodes(nodes):
    # traffic value affects the c value in ubermove
    for node in nodes:
        increaseDecrease = random.randint(0,1)
        if increaseDecrease == 0:
            # Increase
            trafficModifier = random.uniform(0.0, 2.)
        else:
            # Decrease
            trafficModifier = -random.uniform(0.0, 2.)
        
        node.traffic += trafficModifier
        if node.traffic < 1.:
            node.traffic = 1.
        if node.traffic > 5.:
            node.traffic = 5.
        print "Nodeid, traffic:", node.node_id, node.traffic


