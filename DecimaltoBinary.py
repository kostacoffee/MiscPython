def findPower(num):
	power = 0
	while True:
		if (2**power > num):
			return power-1
		power+=1

def decToBin(dec, bin, origPow):
	if (origPow<0):
		return bin
	else:
		currentPowerProduct = 2**(origPow)
		origPow-=1
		if (dec >= currentPowerProduct):
			return decToBin(dec-currentPowerProduct, bin+"1", origPow)
		else:
			return decToBin(dec, bin+"0", origPow)

		
def DecimalToBinary(dec):
	bin = ""
	origPow = findPower(dec)
	return digToBin(dec, bin, origPow)

dec = int(input ("digital "))
print (DecimalToBinary(dec))
input("")