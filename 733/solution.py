def floodFill(image, sr, sc, newColor):
	oldcolor = image[sr][sc]
	imagefill(image,sr,sc,newColor, oldcolor)
	return image

def imagefill(image, x, y, newColor, oldcolor):
	if x == len(image) or y>=len(image[0]) or image[x][y] != oldcolor:
		return
	elif image[x][y] == oldcolor:
		image[x][y] = newColor
		imagefill(image, x+1, y, newColor, oldcolor)
		imagefill(image, x, y+1, newColor, oldcolor)
		imagefill(image, x-1, y, newColor oldcolor)
		imagefill(image, x, y-1, newColor, oldcolor)

