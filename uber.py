from nodes import Node
from passengers import Passenger
import math

# import util
UBER_ID = 0

class Uber:

	## used passenger
	def __init__(self, carId, passengerCount, passengers, x, y, nodePath, currentNode, destinationNode, currentTotalTravelCost):
		self.carId = carId # int starting from 0
		self.passengerCount = passengerCount # int = 0, used count if we maybe do groups later
		self.passengers = passengers # array of passengers in car
		self.x = x # x coord
		self.y = y # y coord
		self.nodePath = nodePath
		self.currentNode = currentNode # current Node() that car is at
		self.destinationNode = destinationNode # Node() that is Passenger() goal
		self.currentTotalTravelCost = currentTotalTravelCost # int starting at 0 on pickup
		global UBER_ID
		UBER_ID += 1

		self.plannedPath = [] # will be filled with ls returned by search alg

	def pickupPassenger(self, passenger):
		if self.currentNode == passenger.start:	
			# print "There is a passenger here at", (self.currentNode.x, self.currentNode.y)
			print "Picked up passenger with ID:", passenger.ID
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
			print "No passenger here to pick up"

	# holding off on deleting this so far, but I think it's sufficient to put into graphs.py
	# def travelToPassengerToPickup(self, node):
	# 	# receive node location of passenger to pickup
	# 	a_star_search()

	# Gets called at every time step
	def setNodePath(self):
		self.nodePath = reconstructPath(a_star_search(self.currentNode, self.destinationNode)[0], self.currentNode, self.destinationNode)

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
			self.destinationNode = None
			# print "Reached destination, dropped off passenger:", self.passengers[0], "at", (self.currentNode.x, self.currentNode.y)
			# print "Total time:", self.currentTotalTravelCost
			finishedID = self.passengers[0]
			del self.passengers[0]
			return finishedID
		else:
			return -1

	# Need to get cost at first step

	def getPathAndCostToDestination(self, currentNode, destinationNode):
		tuple = graph.a_star_search(currentNode, destinationNode)
		path = tuple[0]
		cost = tuple[1]
		print path
		print cost
		# path is the path of nodes to destination
		# do we move one node per time step? 



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


##############################################################
# Testing

# Init
node1 = Node(node_id=1, neighbors=[], passengers=[], x=0.0, y=0.0, traffic=1)
node2 = Node(node_id=2, neighbors=[node1], passengers=[], x=1.0, y=1.0, traffic=1)

car1 = Uber(carId=1, passengerCount=0, passengers=[], x=0.0, y=0.0, nodePath=[], currentNode=node1, destinationNode=None, currentTotalTravelCost=0)
passenger1 = Passenger(node1, node2, 13, 5)

print passenger1.goal.node_id

car1.pickupPassenger(passenger1)
print car1.destinationNode.node_id
# print "Took a time step"
## Moved to node2
#car1.currentNode = node2
car1.uberMove()
car1.uberMove()


car1.reachedDestination()

#car1.uberMove(node2)
