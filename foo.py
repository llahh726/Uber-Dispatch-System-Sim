'''
  Currently being used to test pass_time
  Note(s):
  Reminder(s): in A*, when passenger delivered, remove them from the list of passengers
    can add them to finishedPassengers, which we can use to output data to a file to graph data
'''
from graph import *
from uber import *
from nodes import *
from passengers import *

def main():
    # initialize nodes
    nodes = []
    global PAS_ID
    for xcoord in range(3):
        for ycoord in range(3):
            nodes.append(Node(NODE_ID, [], [], xcoord, ycoord))

    # initialize passengers
    print PAS_ID
    passengers = []
    passengers.append(Passenger(nodes[0], nodes[8], PAS_ID)) #did not set spawn time here
    print PAS_ID
    passengers.append(Passenger(nodes[2], nodes[8], PAS_ID)) #did not set spawn time here
    print PAS_ID

    # initialize ubers
    ubers = []
    ubers.append(Uber(UBER_ID, 0, [], 1, 1, [], nodes[4], nodes[4], 0))

    test = Graph(nodes, passengers, ubers)
    # connect them as a grid
    add_neighbor(nodes[0], nodes[1])   
    add_neighbor(nodes[1], nodes[2])   
    add_neighbor(nodes[3], nodes[4])   
    add_neighbor(nodes[4], nodes[5])   
    add_neighbor(nodes[6], nodes[7])   
    add_neighbor(nodes[7], nodes[8])   
    add_neighbor(nodes[0], nodes[3])   
    add_neighbor(nodes[3], nodes[6])   
    add_neighbor(nodes[1], nodes[4])   
    add_neighbor(nodes[4], nodes[7])   
    add_neighbor(nodes[2], nodes[5])   
    add_neighbor(nodes[5], nodes[8])   

    test.pass_time()
main()
