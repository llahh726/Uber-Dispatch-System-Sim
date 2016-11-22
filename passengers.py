ID_INDEX = 0

class Passenger:
    def __init__(self, xy1, xy2):
        self.start = xy1
        self.goal = xy2
        self.time = 0
        self.pickedUp = False
        self.route = [self.start]

        self.ID = ID_INDEX
        ID_INDEX += 1
