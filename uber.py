from nodes import Node
from passengers import Passenger
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
		if self.currentNode == passenger.start:	
			print "There is a passenger here at", (self.currentNode.x, self.currentNode.y)
			print "Picked up passenger with ID:", passenger.ID
			self.passengers.append(passenger.ID)
			print "Current Passenger list:", self.passengers
			self.destinationNode = passenger.goal
			print "Car's destination node:", (self.destinationNode.x, self.destinationNode.y)
			# time can either start at 0 for the car or be initialized to passenger.time
			self.passengerCount += 1
			print "Passenger count:", self.passengerCount

			# Set the current total time of travel to how long the passenger waited
			# Then add on to that time during travel
			self.currentTotalTravelCost = self.passenger.time
		else:
			# run a* to get there
			print "No passenger to pick up"

	# NEEDS TO BE CALLED At each time step,
	# For all cars that have 1 or more passengers,
	# Check if destination has been reached
	def reachedDestination(self, passenger, currentNode):
		if self.currentNode == self.destinationNode:
			self.passengerCount -= 1
			# return self.currentNode

	def getCarId(self):
		return self.carId

	def getPassengerCount(self):
		return self.passengerCount

	def getPassengers(self):
		return self.passengers

	def getCurrentNode(self):
		return self.currentNode.node_id

	def getDestinationNode(self):
		return self.destinationNode.node_id

	def getCurrTravelCost(self):
		return self.currentTotalTravelCost

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

##############################################################
# Testing
node1 = Node(0, [], [], 0, 0, 1)
node2 = Node(1, [node1], [], 1, 1, 1)
car1 = Uber(1, 0, [], node1, None, 0)

# print car1.getCurrentNode()
# print car1.getCurrTravelCost()

passenger1 = Passenger(node1, node2, 13, 0)

car1.pickupPassenger(passenger1)