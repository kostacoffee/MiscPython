

class Point (object):
	x = 0
	y = 0

	def __init__(self, x,y):
		self.x = int(x)
		self.y = int(y)

directions = ["+x", "+y","-x","-y"]


def getInitPos(size):
	if (size%2 ==0): return Point(size/2-1,size/2-1)
	return Point(size/2,size/2)

def emptySpiral(size):
	spiral = []
	for i in range(size):
		row = []
		for j in range(size):
			row.append(0)
		spiral.append(row)
	return spiral

def changeDir(d):
	return directions[(directions.index(d)+1)%4]

def movePos(pos,stepsUntilTurn, dir):
	if (dir == directions[0]): pos.x += 1
	elif (dir == directions[1]): pos.y +=1
	elif (dir == directions[2]): pos.x -=1
	elif (dir == directions[3]): pos.y -=1 
	return pos
		

def makeSpiral(size):
	spiral = emptySpiral(size)
	number = 1
	stepsUntilTurn = 1
	stepsUntilTurnCounter = 0
	isSecond = False
	pos = getInitPos(size)
	dir = directions[0]
	while (number <= size**2 ):
		spiral[pos.y][pos.x] = number
		pos = movePos(pos,stepsUntilTurn, dir)
		if (stepsUntilTurnCounter == 0):
			dir = changeDir(dir)
			if (isSecond): 
				isSecond = False
				stepsUntilTurn +=1
			else: 
				isSecond = True
			stepsUntilTurnCounter = stepsUntilTurn
		
		number += 1
		stepsUntilTurnCounter -=1
	return spiral
	 
def printSpiral(spiral):
	for i in range(len(spiral)):
		print (spiral[i])

def main():
	size = int(input("How big?"))
	spiral = makeSpiral(size)
	printSpiral(spiral)
	input()


main()