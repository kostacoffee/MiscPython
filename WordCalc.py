DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
OPS = {"plus": "+",
		"minus":"-",
		"times":"*",
		"/":"/"}

def printError(flag):
	if flag == 0 or flag == 2:
		print ("Your %s value is incorrect" % ("second" if flag == 2 else "first"))
	elif flag == 1:
		print ("Your operation is incorrect")
	else:
		print ("Please enter the whole operation")


		"""
def main():
	while True:
		op = ""
		express = raw_input("Enter Calculation: ")
		express = express.split()
		if (len(express) == 3):
			if (express[0] in DIGITS):
				op += str(DIGITS.index(express[0]))
				if(express[1] in OPS):
					op += OPS[express[1]]
					if (express[2] in DIGITS):
						if (DIGITS.index(express[2]) == 0 and express[1] =="/"):
							print ("Can't divide by zero")
							continue
						else:
							op += str(DIGITS.index(express[2]))
							break
					else: printError(2)
				else: printError(1)
			else: printError(0)
		else: printError(-1)
	print eval(op)
	main()
	"""

def main():
	while True:
		op = ""
		exp = raw_input("Enter calculation: ")
		exp = exp.split(" ")
		if (exp[0] in DIGITS and exp[2] in DIGITS):
			exp[0] = str(DIGITS.index(exp[0]))
			exp[2] = str(DIGITS.index(exp[2]))
			if (exp[1] in OPS):
				exp[1] = OPS[exp[1]]
				op = "".join(exp)s
	print eval(op)
	main()

main()