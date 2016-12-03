import node
import passenger
# import util


class Uber:

	# init values - don't think x,y is needed for car if we do it in node
	# used passenger
	def __init__(self, carId, passengerCount = 0, currentNode = Node(), destinationNode = Node(), currentTotalTravelCost = 0):
		self.carId = carId
		self.passengerCount = passengerCount
		self.currentNode = currentNode
		self.destinationNode = destinationNode
		self.currentTotalTravelCost = currentTotalTravelCost

	def pickupPassenger(self, passenger):
		self.destinationNode = passenger.destinationNode
		self.currentTotalTravelCost = 0

	def reachedDestination(self, passenger):
		if self.currentNode == self.destinationNode:
			passengerCount -= 1
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

