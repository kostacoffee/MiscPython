squareSize = ""
firstNum = ""

def again():
	ans = input("Do you want to go again? (Y/N): ")
	if (ans.lower() == "y" or ans.lower() == "yes"):
		main()
		return

def main():
	while True:
		squareSize = input("Please specify the size of the Square (1-9): ")
		if (squareSize.isdigit()):
			squareSize = int(squareSize)
			if (squareSize > 9 or squareSize < 1):
				print("This size is out of the acceptable range.")
			else: break
		else: print ("That is not a number.")

	while True:
		firstNum = input("Please specify the top left number of the Square: ")
		if (firstNum.isdigit()):
			firstNum = int(firstNum)
			if (squareSize >= firstNum and firstNum >= 1): break
			else: print (str(firstNum) + " is not in range of the Square.")
		else: print(firstNum + " is not a number.")

	for i in range(squareSize):
		line = ""
		nums = [j for j in range (firstNum, squareSize+1)]
		if firstNum != 1: 
			nums += [j for j in range (1, firstNum)]
		firstNum += 1
		if (firstNum > squareSize):
			firstNum = 1
		for num in nums:
			line += str(num)
		print (line)
	again()
main()