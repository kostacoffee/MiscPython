def getPrimes(minNum, maxNum):
	primes = []
	for i in range(minNum, maxNum + 1):
		if (isPrime(i)):
			primes.append(str(i))
	return primes

def isPrime(n):
	for i in range (2, n):
		if ((float(n)/i)%1 == 0):
			return False
	return True

def printPrimes(primes):
	length = len(primes)
	if (length == 0): print("There are no primes withon this boundary.")
	elif(length == 1): print("The only prime is " + primes[0])
	else:
		last = primes.pop()
		print("The primes are %s and %s" % (", ".join(primes), last))

def main():
	minNum = int(input("min number"))
	maxNum = int(input("max number"))
	primes = getPrimes(minNum,maxNum)
	printPrimes(primes)
	input()

main()
