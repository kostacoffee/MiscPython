def c(row, index):
    if (index == 0 or index == row): return 1
    else: return c(row-1, index-1) + c(row-1,index)

comb = input("Enter the combination as two comma separated numbers: C(")
comb = comb.split(',')
comb[0] = int(comb[0])
comb[1] = int(comb[1])
print (c(comb[0],comb[1]))
input()