def getTriNum(rank):
	return ((rank**2)+ rank)/2


def findTriNum(number):
	rank = number**0.5
	Trinum1 = getTriNum(rank)
	Trinum2 = getTriNum(rank-1)
	print ("For the Square number \"%i\", the two Triangular numbers are \"%i\" and \"%i\"" % (number ,Trinum1, Trinum2))

def again():
	ans = input("Do you want to go again? (Y/N): ")
	if (ans.lower() == "y" or ans.lower() == "yes"):
		main()
		return

def main():
	number = ""
	while True:
		number = input("Please provide a square number: ")
		if (number.isdigit()):
			number = float(number)
			if ((number**0.5)%1 == 0):
				number = int(number)
				if (number == 1):
					print ("For the square number \"1\", the only triangular number is also \"1\"")
					again()
					return
				else: 
					findTriNum(number)
				break
			else: print ("That's not a square number.")
		else: print("That's not a number.")
	again()
main()