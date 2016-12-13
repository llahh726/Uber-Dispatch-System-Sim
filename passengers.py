'''
    CS182 Final Project
    Ying-ke Chin-Lee, Chris Rodowicz, and Jiacheng Zhao
'''
import util
import random
import sys

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
                came_from, _ = util.a_star_search(uber.currentNode, self.start, True)
                path = util.reconstruct_path(came_from, uber.currentNode, self.start)
                currDist = util.get_path_cost(path)
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
                    came_from, _ = util.a_star_search(uber.currentNode, self.start, True)
                    path = util.reconstruct_path(came_from, uber.currentNode, self.start)
                    currDist = util.get_path_cost(path)
                    # print "currDist=", currDist
                    if (currDist < minDist):
                        minDist = currDist
                        myUber = uber
                    print "there is a uber being assigned!!!!!!!!"

        # optional: change pickedUp value here?
        return myUber


    def info(self):
        return [self.ID, self.start, self.goal, self.time, self.pickedUp, self.route]





