import nodes
import passengers
# import util


class Uber:

	# init values - don't think x,y is needed for car if we do it in node
	# used passenger
	def __init__(self, carId, passengerCount, passengers, currentNode, destinationNode, currentTotalTravelCost):
		self.carId = carId # int starting from 0
		self.passengerCount = passengerCount # int = 0, used count if we maybe do groups later
		self.passengers = passengers # array of passengers in car
		self.currentNode = currentNode # current Node() that car is at
		self.destinationNode = destinationNode # Node() that is Passenger() goal
		self.currentTotalTravelCost = currentTotalTravelCost # int starting at 0 on pickup

	def pickupPassenger(self, passenger):
		self.passengers.append(passenger)
		self.destinationNode = passenger.goal
		# time can either start at 0 for the car or be initialized to passenger.time
		self.passengerCount += 1
		self.currentTotalTravelCost = 0

	def reachedDestination(self, passenger, currentNode):
		if self.currentNode == self.destinationNode:
			self.passengerCount -= 1
			return self.currentNode

	# def graphSearch(problem, frontier):

	# def heuristic(a, b):
	# 	return abs(a.x - b.x) + abs(a.y - b.y)

	# # we have a graph setup right? nodes and edges
	# def aStarSearch(problem, heuristic = nullheuristic):
	# 	frontier = PriorityQueue()
	# 	frontier.push(start)
	# 	visited = {}
	# 	visited[start] = True
	# 	return frontier

node1 = Node(0, [], [], 0, 0, 1)
car1 = Uber(1, 0, [], Node, Node, 0)

