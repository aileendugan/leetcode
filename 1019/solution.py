#head is a singly linked list defined by:
#class listNode:
#	def __init__(self, val=0, next=None):
#		self.val = val
#		self.next = next
def nextLargestNodes(head):
	answer=[]
	new=[]
	while head:
		new.append(head.val)
		head = head.next
	
	check = False

	for i,x in enumerate(new):
		for y in new[i:]:
			if (x>=y):
				continue
			else:
				answer.append(y)
				check = True
		if not check:
			answer.append(0)
		else:
			check = False
	return answer

