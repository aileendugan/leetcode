def mctFromLeafValues(arr):
	i = 0
	while len(arr) > 1:
		val = arr.index(min(arr))
		i += min(arr[val-1:val]+arr[val+1:val+2])* arr.pop(val)
	return i
