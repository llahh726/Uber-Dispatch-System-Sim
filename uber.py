from nodes import Node
from passengers import Passenger
from util import *
UBER_ID = 0

class Uber:

	def __init__(self, carId, passengerCount, passengers, x, y, nodePath, currentNode, destinationNode, currentTotalTravelCost):
		self.carId = carId # int starting from 0
		self.passengerCount = passengerCount # int = 0, used count if we maybe do groups later
		self.passengers = passengers # array of passengers in car
		self.x = x # x coord
		self.y = y # y coord
		self.nodePath = nodePath # list of remaining nodes to move through to reach destination node
		self.currentNode = currentNode # current Node() that car is at, if any
		self.destinationNode = destinationNode # current destination. can be passenger to pick up position or carrying passenger's end goal
		self.currentTotalTravelCost = currentTotalTravelCost # int starting at 0 on pickup
		global UBER_ID
		UBER_ID += 1

	def pickupPassenger(self, passenger):
		if self.currentNode == passenger.start:	
			# print "There is a passenger here at", (self.currentNode.x, self.currentNode.y)
			# print "Picked up passenger with ID:", passenger.ID
			self.passengers.append(passenger.ID)
			# print "Current Passenger list:", self.passengers
			self.destinationNode = passenger.goal
			# print "Car's destination node:", (self.destinationNode.x, self.destinationNode.y)
			# time can either start at 0 for the car or be initialized to passenger.time
			self.passengerCount += 1
			# print "Passenger count:", self.passengerCount

			## Set the current total time of travel to how long the passenger waited
			## Then add on to that time during travel
			self.currentTotalTravelCost = passenger.time
			# print "Passenger wait time:", self.currentTotalTravelCost

		else:
			## run a* to get there
			print "No passenger here to pick up"

	# holding off on deleting this so far, but I think it's sufficient to put into graphs.py
	# def travelToPassengerToPickup(self, node):
	# 	# receive node location of passenger to pickup
	# 	a_star_search()

	# Gets called at every time step
	def setNodePath(self):
		self.nodePath = reconstruct_path(a_star_search(self.currentNode, self.destinationNode)[0], self.currentNode, self.destinationNode)

	# In graph, for all ubers:
	# Each time step is 1. Adds 1 to total travel cost
	# Needs to be passed a node path
	def uberMove(self):
		if self.destinationNode != None:
			targetNode = self.nodePath[0]
			print "My coords:", self.x, self.y
			print "Target coords:", targetNode.x, targetNode.y
			dx = targetNode.x - self.x
			dy = targetNode.y - self.y
			print "Dx:", dx
			print "Dy:", dy
			c = math.sqrt(dx**2 + dy**2)
			print "C:", c

			theta = math.atan(dy / dx)
			print "Theta:", theta
			moveY = math.sin(theta)
			moveX = math.cos(theta)
			print "Move X:", moveX
			print "Move Y:", moveY
			print "Move total", math.sqrt(moveX**2 + moveY**2)
			if c <= 1.0:
				self.x = targetNode.x
				self.y = targetNode.y
				self.currentNode = targetNode
				# move to nextnode in path
				moveToNextTargetNode()
				reachedDestination()
				print "Distance less than 1, reached node and switched to new target"
			else:
				self.x += moveX
				self.y += moveY
				self.currentNode = None
			print "New x:", self.x
			print "New y:", self.y

		self.currentTotalTravelCost += 1
		print "-------------------------"

	def moveToNextTargetNode(self):
		if len(self.nodePath) > 0:
			self.nodePath.pop(0)

	## NEEDS TO BE CALLED At each time step,
	## For all cars that have 1 or more passengers,
	## Check if destination has been reached
	def reachedDestination(self):
		if self.currentNode == self.destinationNode:
			self.passengerCount -= 1
			# return true
			# print "Reached destination, dropped off passenger:", self.passengers[0], "at", (self.currentNode.x, self.currentNode.y)
			# print "Total time:", self.currentTotalTravelCost

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

# Init

# node1 = Node(node_id=1, neighbors=[], passengers=[], x=0.0, y=0.0, traffic=1)
# node2 = Node(node_id=2, neighbors=[node1], passengers=[], x=1.0, y=1.0, traffic=1)
# car1 = Uber(carId=1, passengerCount=0, passengers=[], x=0.0, y=0.0, nodePath=[], currentNode=node1, destinationNode=None, currentTotalTravelCost=0)
# passenger1 = Passenger(node1, node2, 13, 5)

# print passenger1.goal.node_id

# car1.pickupPassenger(passenger1)
# print car1.destinationNode.node_id
# # print "Took a time step"
# ## Moved to node2
# #car1.currentNode = node2
# car1.uberMove()
# car1.uberMove()



# node1 = Node(0, [], [], 0, 0, 1)
# node2 = Node(1, [node1], [], 1, 1, 1)
# car1 = Uber(1, 0, [], node1, None, 0)

# node1 = Node(node_id=1, neighbors=[], passengers=[], x=0.0, y=0.0, traffic=1)
# node2 = Node(node_id=2, neighbors=[node1], passengers=[], x=1.0, y=1.0, traffic=1)

# car1 = Uber(carId=1, passengerCount=0, passengers=[], x=0.0, y=0.0, nodePath=[], currentNode=node1, destinationNode=None, currentTotalTravelCost=0)

# passenger1 = Passenger(node1, node2, 13, 5)


# car1.pickupPassenger(passenger1)
# # print "Took a time step"
# ## Moved to node2

# car1.currentNode = node2
# car1.reachedDestination()

# #car1.currentNode = node2
# car1.uberMove()
# car1.uberMove()
# >>>>>>> ead9c74c08bf7813856621123ee5b92b2cce3d37


# # car1.reachedDestination()

# # #car1.uberMove(node2)
