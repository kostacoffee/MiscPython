import os.path
ORD_OFFSET = 97
E_POS = 4

def initFreqList():
	frList = []
	for i in range(26):
		frList.append(0)
	return frList

def initText(filepath):
	words = ""
	for line in open(filepath):
		words += line + " "
	words = removeSpaces(words)
	return words

def removeSpaces(text):
	while text.find(" ") != -1:
		index = text.find(" ")
		text = text[:index] + text[index+1:]
	return text

def fillFreqList(text, freqList):
	for char in text:
		if (char.isalpha()):
			freqList[ord(char)-ORD_OFFSET] += 1
	return freqList

def mostCommonChar(freqList):
	highValue = max(freqList)
	eIndex = freqList.index(highValue)
	freqList.remove(highValue)
	return eIndex

def DecypherText(text, shift):
	decText = ""
	for char in text:
		if (ord(char) >= 97 and ord(char) <= 97+26):
			decChar = ((ord(char) - ORD_OFFSET) + shift)%26
			decText += chr(decChar+ ORD_OFFSET)
	return decText

def writeFile(text,filepath):
	with open("dec" + filepath, 'w') as decFile:
		decFile.write(text)
	print("Decrypted file created with the name %s" % ("dec" + filepath))

filepath = ""
while True:
	filepath = input("Please provide the file name with the encrypted text: ")
	if (os.path.isfile(filepath)): break
	print("This file doesn't exist.")
letterFreq = initFreqList()
text = initText(filepath)
letterFreq = fillFreqList(text, letterFreq)
for i in range(3):
	eIndex = mostCommonChar(letterFreq)
	shift = E_POS - eIndex
	text = DecypherText(text, shift)
	if (len(text)>= 40):
		print (text[:40])
	else: print (text)
	test = input ("Does this text look right?")
	test = test.lower()
	if (test == "yes" or test == "y"):
		writeFile(text, filepath)
		break
	else: print ("Trying another shift...")
else: print ("Sorry, this text is not encrypted with the Caesar Cypher.")
input("Press Enter to exit.")

