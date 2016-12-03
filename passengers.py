import random
ID_INDEX = 0

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

def main():
    nodes = ['a', 'b', 'c', 'd', 'e'] # random stuff just to get started
    spawn(10, nodes)
main()

