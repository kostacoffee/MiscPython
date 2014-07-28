

def printResult(number, multPer, multRoot, addPer, addRoot):
	print("For the integer " + str(number) + ":")
	print("Multiplicative Persistence: " + str(multPer))
	print("Multiplicative Root: " + str (multRoot))
	print ("Additive Persistence: " + str(addPer))
	print ("Additive Root: " + str(addRoot))

def rootsPersistencesAdd(number, addPer):
	if (len(str(number)) == 1):
		return number
	else:
		digitAdd = str(number)
		number = int(digitAdd[0])
		for digit in digitAdd[1:]:
			number+=int(digit)
		addPer[0]+=1
		return rootsPersistencesAdd(number, addPer)
	
def rootsPersistencesMult(number, multPer):
	if (len(str(number)) == 1):
		return number
	else: 
		digitMult = str(number)
		number = int(digitMult[0])
		for digit in digitMult[1:]:
			number*=int(digit)
		multPer[0]+=1
		return rootsPersistencesMult(number, multPer)

def rootsPersistences(number):
	multPer = [0]
	multRoot = 0
	multRoot = rootsPersistencesMult(number, multPer)
	addPer = [0]
	addRoot = 0
	addRoot = rootsPersistencesAdd(number, addPer)
	printResult(number, multPer[0], multRoot, addPer[0], addRoot)

def again():
	ans = input("Do you want to go again? (Y/N): ")
	if (ans.lower() == "y" or ans.lower() == "yes"):
		main()
		return

def main():
	while True:
		number = input("Please provide an positive integer: ")
		if (number.isdigit()):
			if (len(str(number)) >= 1): 
				number = int(number)
				break
			if (number < 0):
				return number
			else: printResult (number)
		else: print("That's not a number.")
	rootsPersistences(number)
	again()

main()

			
	


