def getNeighbors(distance,node):
	return node[1]
def getEdge(node):
	return node[2]
def getmin(distance):
	return distance.pop()

def networkDelayTime(times, N, K):
	diction = dict()
	for i in times:
		distance.append(i)
	while distance:
		node = getmin(distance)
		neighbors = getNeighbors(node)
		for n in neighbors:
			w = getEdge(n)
			if diction[n]+w < diction[n]:
				diction[n] = (diction[n]+w, node)
	return diction[K]


