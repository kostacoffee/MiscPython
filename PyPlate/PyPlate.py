"""
Pyplate.py

A program that asks the user for their desired numebr plate,
checks for its existence in the database and that the numbher plate is valid and acceptable
registers the number plate into the file, adding the price to the total.

Author: Konstantin Dunn
Date: 22/03/2013
"""

#Constants
WORD_FILE = "words.txt"
PLATES = "regged.txt"
RESTRICTED_WORDS = "restricted.txt"
EXPENSIVE_PLATE = 120
CHEAP_PLATE = 80
#/Constants

#quick way for checking string in file:
#<http://stackoverflow.com/questions/4940032/search-for-string-in-txt-file-python>

#Returns True if the plate is already registered
def isRegged(plate):
	return (plate in open(PLATES).read())

#Returns True if the edited plate without numbers is in the "restricted.txt" file or has special characters
def isRestricted(plate):
	if plate == "": return False
	else:
		return (plate in open(RESTRICTED_WORDS).read())

#Returns True if the edited plate without numbers is in the "words.txt" file
def isRealWord(plate):
	return (plate in open(WORD_FILE).read())

#Returns an edited string of plate with all non letter digits removed
def plateLetters(plate):
	noDigits = ""
	for char in plate:
		if (char.isalpha()):
			noDigits+=char
	return noDigits 

def register(plate):
	f = open(PLATES, 'a')   #__exit__ Attribute error. chaged "with (PLATES, 'a') as plateFile:" to standard open/close procedure <http://stackoverflow.com/questions/5773545/python-3-2-with-as-not-working>
	f.write(plate+"\n")
	f.close()

def updatePrice(plate):
	price = 0
	if (isRealWord(plate)):       #Tried to check with numbers. Changed plate to plateLetters(plate), since a word with numbers does not exist.
		price = EXPENSIVE_PLATE
	else:
		price = CHEAP_PLATE
	print("Congrats, You just added %s for $%i" % (plate, price))
	return price

def main():
	regs = 0
	totalCost = 0
	print("Welcome to PythonPlate!\nPlease enter your desired Car number plate, or if you are finished, type \"-1\"")
	while True:
		plate = input("Please input plate: ")
		if plate == "-1": break
		if len(plate) == 6:
			plate = plate.upper()
			if (not isRegged(plate) and not isRestricted(plateLetters(plate)) and plate.isalnum()):
				register(plate)
				totalCost += updatePrice(plate)
				regs+=1
			else: print ("Not available")    
		else: print ("That's the wrong length. It must be 6 characters!")
			
	if (regs> 0):
		print("-------------------------\n\nSuccessful registrations: %i\nTotal Cost: $%i\n\n-------------------------" % (regs, cost))
		input()
	else:
		print ("No Registrations have been made")
		retry = input ("Do you want to re-try (Y/N) ? ")
		retry = retry.lower()
		if (retry == "y" or retry == "yes"):
			main()
main()
