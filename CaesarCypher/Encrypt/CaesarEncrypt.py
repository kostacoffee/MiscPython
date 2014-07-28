import os.path

alph = "abcdefghijklmnopqrstuvwxyz"
print("Welcome to Caesar Cypher Encryption")
while True:
	filename = input("Please type in the file name containing the text you would like to encrypt: ") 
	if (os.path.exists(filename)) : break
	print ("This file does no exist")
encindex = 0
while True:
	encindex = input("Please input the encryption index you would like to use (1 - 25): ")
	if (encindex.isdigit()):
		encindex = int(encindex)
		if (encindex >=1 and encindex <= 25):
			 break
		else: print ("Please provide a number between 1 and 25.")
	else: print ("Please provide a number")
with open(filename, 'r') as text:
	encFile =  open("enc" + filename, 'w')
	while True:
		c = text.read(1)
		if not c:
			encFile.close()
			break
		else:
			if (c.isalpha()):
				cindex = alph.find(c.lower())
				ca = alph[(cindex + encindex) % len(alph)]
				encFile.write(alph[(cindex + encindex) % len(alph)])
			else:
				encFile.write(c)

print("Encrypted file created with the name %s" % ("enc" + filename))
input("Press Enter to exit.")
	