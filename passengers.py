'''
  TODO:
    - passenger find closest uber
    - do a simulation for pass_time to make sure that it works 
      - integrate this with timestep = 1
'''

import random
import nodes
from sys import * #trying to avoid that weirdo error (since sys is imported in graph.py)

ID_INDEX = 0

class Passenger:
    def __init__(self, node1, node2, idInt=0,  num=0):
        self.start = node1
        self.goal = node2
        self.time = num
        self.pickedUp = False
        
        self.route = [self.start] # we may not use this (can use the uber's route)

        self.ID = idInt

    def closestUber(self, ubers):
        if self.pickedUp: # then don't claim any uber
            return None

        minDist = sys.maxsize
        myUber = None
        for uber in ubers:
            if uber.passengerCount == 0:
                currDist = get_euc_dist(self.start, uber.currentNode)
                if (currDist < minDist):
                    minDist = currDist
                    myUber = uber
        # optional: change pickedUp value here?
        return myUber

    def info(self):
        return [self.ID, self.start, self.goal, self.time, self.pickedUp, self.route]

# n = num to spawn
def spawn(n, nodes):
    global ID_INDEX
    # work in progress: where do I get the coordinates?
    passengers = []
    # so nodes would actually have to be made first
    for i in xrange(n):
        passengers.append(Passenger(random.choice(nodes), random.choice(nodes), ID_INDEX))
        ID_INDEX += 1

    for p in passengers:
        print p.info()

    # return passengers

def main():
    nodes = ['a', 'b', 'c', 'd', 'e'] # random stuff just to get started
    spawn(10, nodes)
main()

