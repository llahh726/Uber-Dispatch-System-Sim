#import node
import util

class uber:

	# init values
	def __init__(self, carId, posX = 0, posY = 0, carryingPassenger = false, currentNode = Node(), currentTravelCost = 0):
		self.carId = carId
		self.posX = posX
		self.posY = posY
		self.carryingPassenger = carryingPassenger
		self.currentNode = currentNode
		self.currentTravelCost = currentTravelCost

	def reachedDestination(self):








	def graphSearch(problem, frontier):

	def heuristic(a, b):
		return abs(a.x - b.x) + abs(a.y - b.y)

	# we have a graph setup right? nodes and edges
	def aStarSearch(problem, heuristic = nullheuristic):
		frontier = PriorityQueue()
		frontier.push(start)
		visited = {}
		visited[start] = True
		return frontier

