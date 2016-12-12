from nodes import Node
from passengers import Passenger
from util import *
import math, sys

class Uber:
	UBER_ID = 0
	def __init__(self, passengerCount, passengers, x, y, nodePath, currentNode, destinationNode, currentTotalTravelCost, assigned_passenger):
		self.carId = Uber.UBER_ID # int starting from 0
		self.passengerCount = passengerCount # int = 0, used count if we maybe do groups later
		self.passengers = passengers # array of passengers in car
		self.x = x # x coord
		self.y = y # y coord
		self.nodePath = nodePath # list of remaining nodes to move through to reach destination node
		self.currentNode = currentNode # current Node() that car is at, if any
		self.destinationNode = destinationNode # current destination. can be passenger to pick up position or carrying passenger's end goal
		self.currentTotalTravelCost = currentTotalTravelCost # int starting at 0 on pickup
		self.assigned_passenger = assigned_passenger
		Uber.UBER_ID += 1

	def closestPassenger(self, passengers):
		minDist = sys.maxsize
		myPass = None
		for p in passengers:
			if not p.got_uber:
				came_from, _ = a_star_search(self.currentNode, p.start, True)
				path = reconstruct_path(came_from, self.currentNode, p.start)
				currDist = get_path_cost(path)
				if (currDist < minDist):
					minDist = currDist
					myPass = p
		return myPass

	def pickupPassenger(self):
		if len(self.assigned_passenger) == 1:
			asseigned_p = self.assigned_passenger[0]
			if self.currentNode == asseigned_p.start:	
				# print "There is a passenger here at", (self.currentNode.x, self.currentNode.y)
				# print "Picked up passenger with ID:", passenger.ID
				self.passengers.append(asseigned_p)
				# print "Current Passenger list:", self.passengers

				# print "Car's destination node:", (self.destinationNode.x, self.destinationNode.y)
				# time can either start at 0 for the car or be initialized to passenger.time
				self.passengerCount += 1

					# pool -> if 1 passenger, if 2 passenger
				if len(self.passengers) == 1:
					self.destinationNode = asseigned_p.goal
				elif len(self.passengers) == 2:
					# the closer one of the two
					came_from1, _ = a_star_search(self.currentNode, self.passengers[0].goal, True)
					came_from2, _ = a_star_search(self.currentNode, self.passengers[1].goal, True)
					path1 = reconstruct_path(came_from1, self.currentNode, self.passengers[0].goal)
					path2 = reconstruct_path(came_from2, self.currentNode, self.passengers[1].goal)
					dist1 = get_path_cost(path1)
					dist2 = get_path_cost(path2)
					# print "currDist=", currDist
					if (dist1 <= dist2):
					    self.destinationNode = self.passengers[0].goal
					else:
						self.destinationNode = self.passengers[1].goal
				else:
					print 'error, pass >= 2!'

				self.currentTotalTravelCost = asseigned_p.time
				# print "Passenger wait time:", self.currentTotalTravelCost
				asseigned_p.pickedUp = True
				self.assigned_passenger.remove(asseigned_p)

		elif len(self.assigned_passenger) == 2:
			for asseigned_p in self.assigned_passenger:
				if self.currentNode == asseigned_p.start:
					self.passengers.append(asseigned_p)
					self.passengerCount += 1
					# check
					if self.passengerCount != 1:
						print 'error here in number of passengers to pick up'
					self.currentTotalTravelCost = asseigned_p.time
					asseigned_p.pickedUp = True
					self.assigned_passenger.remove(asseigned_p)
			# to pick up the other guy
			self.destinationNode = self.assigned_passenger[0].start
		else:
			print 'len of assigned_passenger not 1 or 2, error'

	# Gets called at every time step
	def setNodePath(self):
		#print "ASTAR", a_star_search(self.currentNode, self.destinationNode)[0]
		self.nodePath = reconstruct_path(a_star_search(self.currentNode, self.destinationNode)[0], self.currentNode, self.destinationNode)[1:]
		#print "Self.nodePath", self.nodePath

	# In graph, for all ubers:
	# Each time step is 1. Adds 1 to total travel cost
	# Needs to be passed a node path
	def uberMove(self):
		#print "Uber passengers", self.passengers
		# print "Destination node:", self.destinationNode
		if self.destinationNode != None:
			if not self.nodePath:
				self.reachedDestination()
			else:
				targetNode = self.nodePath[0]
				#print "My coords:", self.x, self.y
				#print "Target coords:", targetNode.x, targetNode.y
				dx = targetNode.x - self.x
				dy = targetNode.y - self.y
				#print "Dx:", dx
				#print "Dy:", dy
				c = math.sqrt(dx**2 + dy**2)
				#print "C:", c
				# account for 0
				if dx == 0:
					if dy > 0:
						theta = math.pi/4
					elif dy < 0:
						theta = math.pi/-4
					else:
						theta = 0.0
				elif dx < 0:
					theta = math.atan(dy / dx) + math.pi
				else:
					theta = math.atan(dy / dx) 

				#print "Theta:", theta
				# VARYING NODE COST TESTING
				moveY = math.sin(theta) / targetNode.traffic
				moveX = math.cos(theta) / targetNode.traffic

				# Old working version
				# moveY = math.sin(theta)
				# moveX = math.cos(theta)
				#print "Move X:", moveX
				#print "Move Y:", moveY
				#print "Move total", math.sqrt(moveX**2 + moveY**2)
				# if c < 1.0:
				if c < (1.0 / targetNode.traffic):
					self.x = targetNode.x
					self.y = targetNode.y
					self.currentNode = targetNode
					# move to nextnode in path
					# self.moveToNextTargetNode()

					self.reachedDestination()
					#print "Distance less than 1, reached node and switched to new target"
				else:
					self.x += moveX
					self.y += moveY
					self.currentNode = None
				#print "New x:", self.x
				#print "New y:", self.y

		self.currentTotalTravelCost += 1
		#print "-------------------------"

	def moveToNextTargetNode(self):
		if len(self.nodePath) > 0:
			self.nodePath.pop(0)

	## NEEDS TO BE CALLED At each time step,
	## For all cars that have 1 or more passengers,
	## Check if destination has been reached
	def reachedDestination(self):
		if self.currentNode == self.destinationNode:
			if self.assigned_passenger:
				self.pickupPassenger()

			# dropping passenger off
		for p in self.passengers:
			if self.currentNode == p.goal:
				# mark true so passenger could be removed
				p.arrived = True
				self.passengers.remove(p)
				if self.passengers:
					self.destinationNode = self.passengers[0].goal
				else:
					self.destinationNode = None
				# print self.passengerCount
				self.passengerCount -= 1
				# print self.passengerCount
				#print 'journey done!!!!'
			# return true
			# print "Reached destination, dropped off passenger:", self.passengers[0], "at", (self.currentNode.x, self.currentNode.y)
			#print "Self.pass count:", self.passengerCount
			#self.passengerCount -= 1
			#print "Self.pass count after:", self.passengerCount
			# self.destinationNode = None

			#print "Reached destination, dropped off passenger:", self.passengers[0], "at", (self.currentNode.x, self.currentNode.y)
			#print "Self.passengers:", self.passengers
			#self.passengers.pop(0)
			#print "Self.passengers after pop:", self.passengers
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
