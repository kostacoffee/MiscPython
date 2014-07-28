def permutation(inp, out):
    if (len(inp) == 0):
        print(out)
        return
    else:
        for l in inp:
            inStr = inp.replace(l, "")
            permutation(inStr, out+l)

def printPermutations(inp):
	permutation(inp, "")

printPermutations(input("Enter a set of characters for which you want to see all permutations: "))
input()