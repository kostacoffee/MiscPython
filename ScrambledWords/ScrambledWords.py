import os.path
import random


def searchForPunct(word):
	punct = []
	for i in range(len(word)):
		if (not word[i].isalpha()):
			punct.append(word[i])
	return punct

def scramblePunct(words, punct):
	fullWord = ""
	if (type(words) == str):
		return scramble(words)
	for i in range(len(words)):
		if (len(punct) >0):
			fullWord += scramble(words[i]) + punct[i]
			punct.pop(i)
		else: fullWord += scramble(words[i])
	return fullWord

def scramble(word):
	wordCopy = word
	scrWord = word[0] + word[len(word)-1]
	tempscr = ""
	word = word[1:len(word)-1]
	chars = list(word)
	while len(tempscr) < len(word):
		ranIndex = random.randint(0, len(chars)-1)
		tempscr += chars[ranIndex]
		chars.pop(ranIndex)
	if (wordCopy == scrWord):
		scramble(scrWord)
	return scrWord[0] + tempscr + scrWord[1:]

def scrambleWord(word):
	if (word.isalpha()):
		return scramble(word) + " "
	else:
		punct = searchForPunct(word)
		endpunct = ""
		beginpunct= ""
		while (not word[0].isalpha()):
			beginpunct += word[0]
			punct.remove(beginpunct[len(beginpunct)-1])
			word = word[1:]
		while (not word[len(word)-1].isalpha()):
			endpunct += word[len(word)-1]
			punct.remove(endpunct[len(endpunct)-1])
			word = word[:len(word)-1]
		if (word[len(word)-2:] == "'s"):
			endpunct = "'s" + endpunct
			punct.remove("'")
			word = word[:len(word)-2]
		words = word
		for p in punct:
			words = word.split(p)
		return beginpunct + scramblePunct(words, punct) + endpunct + " "


def scrambleLine(line):
	words = line.split(" ")
	scrWords = []
	while(words.__contains__("")):
	   words.remove("")
	for word in words:
		if (len(word) > 3):
			scrWords.append(scrambleWord(word))
		else: scrWords.append(word + " ")
	return scrWords

filepath = ""
while True:
	filepath = input("Please provide a file you would like to use for scrambling. ")
	if (os.path.isfile(filepath)):	break
	print ("That file does not exist")

with open(filepath,'r') as file:
	scrambledFile = open("scr" + filepath, 'w')
	for line in file:
		scrLine = scrambleLine(line)
		for word in scrLine:
			scrambledFile.write(word)
	scrambledFile.close()
input("Press Enter to exit")
