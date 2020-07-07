import heapq

class Node:
	def __init__(self, val, weight):
		self.val = val
		self.weight = weight
		self.next = None
class Alist:
	def __init__(self):
		self.list=[]

	def addNode(self, n):
		self.list.append(n)
	
	def addEdge(self, n1, n2):
		new2 = Node(n2.val)
		end = n1.next
		n1.next = new2
		new2.next = end

	def getNeighbors(self, n):
		new = []
		while n.next:
			new.append(n.next)
			n = n.next
		return new
	def getEdge(self, node, n):
		while node.next:
			if node == n:
				return node.weight
			node = node.next
def networkDelayTime(times, N, K):
	distance_heap = []
	for i in times:
		distance_heap.append(times[i][2], times[i][1]))
	#use heapq to make this a min heap above
	adjlist = Alist()
	times_dict = dict()
	for i in range(N):
		adjlist.addNode(i+1,0)
	for f, t , w in times:
		adjlist.addEdge(Node(f,0),Node(t,w))
	
	for i in range(len(times)):
		n1 = Node(times[i][0])
		n2 = Node(times[i][1])
		adjlist.addEdge(n1, n2) #we only want to go one direction mate

	for i in range(len(times)):
		times_dict.update({times[i][2] : (times[i][2], INT_MAX)}) #initialize dictionary to infinity for each weight and make its prev node itself

	times_dict.update({ K : (K, 0)})
	
	while distance_heap:
		(distance,node) = distance_heap.dequeue()
		neighbors = adjlist.getNeighbors(node)
		for n in neighbors:
			w = adjlist.getEdge(node,n) #get edge from adjacency list
			if distance+w < times_dict[n][1]: # if the distance of that node to its neighbor node is less than the distance in the dictionary for that neighbor node, update it
				time_dict[n] = (node, distance+w)
			


