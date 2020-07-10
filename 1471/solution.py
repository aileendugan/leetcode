def getStrongest(arr, k):
	strongest = []
	arr.sort()
	if len(arr) % 2:
		middle = len(arr) // 2
	else:
		middle = len(arr) // 2 - 1
	median = arr[middle]
	i = 0
	j = len(arr) - 1
	while (len(strongest) != k):
		newi = abs(arr[i] - median)
		newj = abs(arr[j] - median)
		if newj >= newi:
			strongest.append(arr[j])
			j -= 1
		else:
			strongest.append(arr[i])
			i += 1
	return strongest
	
