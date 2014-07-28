import random

LEXICON_FILE = "lexicon.txt"
NUM_LIVES = 5

class Hangman(object):
	lexicon = LEXICON_FILE

	def __init__(self):
		self.linenum = self.countLines(self.lexicon)
		self.lives = NUM_LIVES
		self.word = self.getWord(self.linenum)
		self.uWord = self.underscore(self.word)
		self.usedLetters = []

	def isDead(self):
		if (self.lives == 0):
			print ("Sorry, you could not beat this word.")
			print ("The word was " + self.word)
			return True

	def findOccurences(self, letter):
		occurences = []
		startIndex = -1
		while (self.word.find(letter, startIndex+1) != -1):
			index = self.word.find(letter,startIndex+1)
			occurences.append(index)
			startIndex = index
		return occurences
				

	def getLetter(self):
		letter = input ("Input a letter that could be part of the word: ")
		while (True):
			if (letter.isalpha):
				if (len(letter) == 1):
					self.processLetter(letter.upper())
					break
				else:
					print ("Please provide only one letter.")
			else: 
				print ("This is not a letter.")
			self.getLetter()
			return

	def processLetter(self,letter):
		occurences = self.findOccurences(letter)
		if (not letter in self.usedLetters):
			self.usedLetters.append(letter)
			if (len(occurences) > 0):
				wordCopy = self.word
				for i in occurences:
					self.uWord = self.uWord[:i] + letter + self.uWord[i+1:]
			else: self.lives -= 1
		else: 
			print ("This letter has been used")
			self.getLetter()

	def printState(self):
		print ("")
		print("You have %i li%s" % (self.lives, "ves" if self.lives > 1 else "fe"))
		print("Your word looks like this: " + self.uWord)
		print("Used Letters: %s" % (", ".join(self.usedLetters)))

	def underscore(self, word):
		uWord = ""
		for i in range(len(word)):
			uWord += "_"
		return uWord

	def countLines(self, lexFilename):
		counter = 0
		with open(lexFilename, "r") as lex:
			for line in lex:
				counter +=1
		return counter

	def getWord(self, linenum):
		lineIndex = random.randint(0, linenum)
		lineCounter = 0
		with open(self.lexicon,"r") as lex:
			for line in lex:
				if lineCounter == lineIndex:
					return line.rstrip()
				lineCounter +=1

	def victoryMsg(self):
		print("Well done!! You beat the word and you still have %i lives left!" % (self.lives))

def again():
	ans = input("Would you like to play again? ")
	ans = ans.lower()
	return (ans == "y" or ans == "yes")


def main():	
	print ("Welcome to Hangman")
	while True:
		hangman = Hangman()
		while hangman.word != hangman.uWord:
			hangman.printState()
			hangman.getLetter()
			if (hangman.isDead()): break
		else: hangman.victoryMsg()
		if (not again()): break
main()