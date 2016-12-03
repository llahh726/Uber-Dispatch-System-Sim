import random

MAX_X = 10
MAX_Y = 10

class Passenger:
    def __init__(self, node1, node2, idInt,  num=0):
        self.start = node1
        self.goal = node2
        self.time = num
        self.pickedUp = False
        # keep track of which Uber picked passenger up or not?
        self.route = [self.start]

        self.ID = idInt

    def info(self):
        return [self.ID, self.start, self.goal, self.time, self.pickedUp, self.route]

# n = num to spawn
def spawn(n):
    # work in progress: where do I get the coordinates?
    passengers = []
    ID_INDEX = 0
    # so nodes would actually have to be made first
    for i in xrange(n):
        passengers.append(Passenger(random.choice(nodes), random.choice(nodes), ID_INDEX))
        ID_INDEX += 1

    for p in passengers:
        print p.info()

def main():
    spawn(10)
main()

