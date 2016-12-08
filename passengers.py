'''
  TODO:
    - passenger find closest uber
    - do a simulation for pass_time to make sure that it works 
      - integrate this with timestep = 1
'''

import random
import nodes
import sys
#from sys import * #trying to avoid that weirdo error (since sys is imported in graph.py)
from util import *

class Passenger:
    PAS_ID = 0
    def __init__(self, node1, node2, num=0):
        self.start = node1
        self.goal = node2
        self.time = num
        self.pickedUp = False
        self.arrived = False
        self.got_uber = False
        
        self.route = [self.start] # we may not use this (can use the uber's route)
        #print "INIT:", PAS_ID
        self.ID = Passenger.PAS_ID
        Passenger.PAS_ID += 1

    def closestUber(self, ubers):
        minDist = sys.maxsize
        myUber = None
        for uber in ubers:
            #print "myUber:", myUber, "dnode=", uber.destinationNode
            if uber.destinationNode == None:
                came_from, _ = a_star_search(uber.currentNode, self.start, True)
                path = reconstruct_path(came_from, uber.currentNode, self.start)
                currDist = get_path_cost(path)
                # print "currDist=", currDist
                if (currDist < minDist):
                    minDist = currDist
                    myUber = uber
        # optional: change pickedUp value here?
        return myUber

    # returns the uber that has the potential to pool
    def closestUber_pool(self, ubers):
        minDist = sys.maxsize
        myUber = None
        for uber in ubers:
            #print "myUber:", myUber, "dnode=", uber.destinationNode
            if (uber.destinationNode) == None or (len(uber.assigned_passenger) <= 1  and 
                uber.passengerCount <= 1) and (len(uber.assigned_passenger) + uber.passengerCount  < 2):
                if uber.currentNode:
                    came_from, _ = a_star_search(uber.currentNode, self.start, True)
                    path = reconstruct_path(came_from, uber.currentNode, self.start)
                    currDist = get_path_cost(path)
                    # print "currDist=", currDist
                    if (currDist < minDist):
                        minDist = currDist
                        myUber = uber
                    print "there is a uber being assigned!!!!!!!!"

        # optional: change pickedUp value here?
        return myUber


    def info(self):
        return [self.ID, self.start, self.goal, self.time, self.pickedUp, self.route]

# n = num to spawn
def spawn(n, nodes):
    global PAS_ID
    # work in progress: where do I get the coordinates?
    passengers = []
    # so nodes would actually have to be made first
    for i in xrange(n):
        passengers.append(Passenger(random.choice(nodes), random.choice(nodes), PAS_ID))
        #PAS_ID += 1

    for p in passengers:
        print p.info()

    # return passengers



