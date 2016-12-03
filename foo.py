'''
  Putting this in a separate file for now (can probably merge a bunch of this with Graph class)
  Rough sketch of how we might set up the setup part
  Will need:
    spawn() 
    Possibly global vars:
      nodes[] 
      cars[]
      passengers[]
  Reminder: in A*, when passenger delivered, remove them from the list of passengers
'''
import sys, uber

time = 10 # some number that we set, and we can just leave the passengers who were unlucky enough to spawn too late

def main():
    spawnTimes = [1, 3, 4] # maybe keep a list of times at which to spawn someone
    spawnQueue = ['a','b','c'] # list of passengers that we want to spawn at above times (arrays must be same len)
    for step in time:
        if step == spawnTimes[0]: # spawn and remove from queue
            spawn(spawnQueue[0])
            del spawnQueue[0]
            del spawnTimes[0]
        # assign unassigned cars to nearest passengers
        for car in cars:
            if car.passengerCount == 0:
                minDist = sys.maxsize
                assignedTo = None # not sure if this is a proper initialization
                for p in passengers:
                    if (not p.pickedUp): # just look at passengers who need a ride
                        currDist = get_euc_dist(car.currentNode, p.start)
                        if (minDist > currDist):
                            minDist = currDist
                            assignedTo = p
                car.pickupPassenger(assignedTo)
                assignedTo.pickedUp = True

        for p in passengers: # increment their time in the system
            p.time += 1
main()
