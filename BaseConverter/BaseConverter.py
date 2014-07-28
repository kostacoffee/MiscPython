def ConvToBase(decimal, convBase, convNum, bases):
	if (decimal == 0):
		return convNum[::-1]
	else:
		baseValue = decimal%convBase
		character = bases[baseValue]
		return ConvToBase(int(decimal/convBase), convBase,convNum+character, bases) 


def ConvToDec(orig, origBase, decimal, bases):
	if (len(orig) == 0):
		return decimal
	else:
		decimal += bases.index(orig[0])
		if (len(orig) != 1):
			decimal *= origBase
		return ConvToDec(orig[1:], origBase, decimal, bases)


def ConvertToBase(orig, origBase, convBase, bases):
	decimal = 0
	decimal = ConvToDec(orig, origBase, decimal, bases)
	if (convBase == 10): return decimal
	convNum = ""
	return ConvToBase(decimal, convBase, convNum, bases)

def biggestNum(baseStr, bases):
	highestVal = -1
	for char in bases:
		if (baseStr.find(char) != -1):
			highestVal = bases.index(char)
	return highestVal

def fillBases():
	bases = ""
	with open("bases.txt", "r") as baseFile:
		for line in baseFile:
			bases += line
	return bases

def printBaseError():
	print ("This number is out of the range of bases provided.\nPlease fill in the bases.txt file or choose a different number.")

def getNum(bases):
	orig = ""
	while True:
		orig = input ("What's the number you want to convert? ")
		if (biggestNum(orig, bases) != -1): return str(orig)
		else: printBaseError()

def getBase(bases, flag):
	base = ""
	while True:
		if (flag == 0):
			base = input ("What base is this in? ")
		else : base = input ("What base do you want to convert it to? ")
		if (base.isdigit()):
			base = int(base)
			if (base <= len(bases) and base > 1):
				return base
			else: printBaseError()
		else: print("Please provide a number!")

bases = fillBases()
while True:
	orig = getNum(bases)
	origBase = getBase(bases, 0)
	convBase = getBase(bases, 1)
	print (ConvertToBase(orig, origBase, convBase, bases))
	ans = input("Want to go again? (Y/N) ")
	ans = ans.lower()
	if (ans != "y" and ans != "yes"): break