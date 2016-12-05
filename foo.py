'''
  Currently being used to test pass_time
  Note(s):
    - look into PAS_ID for including inside passenger.py
      - in which case remove it from graph.py
  Reminder(s): in A*, when passenger delivered, remove them from the list of passengers
    can add them to finishedPassengers, which we can use to output data to a file to graph data
'''
from graph import *
from uber import *
from nodes import *
from passengers import *
from sys import *

def main():
    # initialize nodes
    nodes = []
    PAS_ID = 0
    for xcoord in range(3):
        for ycoord in range(3):
            nodes.append(Node(NODE_ID, [], [], xcoord, ycoord))

    # initialize passengers
    passengers = []
    passengers.append(Passenger(nodes[0], nodes[8], PAS_ID)) #did not set spawn time here

    # initialize ubers
    ubers = []
    ubers.append(Uber(UBER_ID, 0, [], nodes[4], nodes[4], 0))

    test = Graph(nodes, passengers, ubers)
    # connect them as a grid
    
main()
