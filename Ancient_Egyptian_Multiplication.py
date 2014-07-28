def mult(nums):
	product = 0
	while (nums[1] !=1):
		if (nums[1] % 2  != 0):
			product += nums[0]
		nums[0] *= 2
		nums[1] /= 2
		nums[1] = int(nums[1])
	product += nums[0]
	print("the product is " + str(product))

def again():
	ans = input("Do you want to go again? (Y/N): ")
	if (ans.lower() == "y" or ans.lower() == "yes"):
		main()
		return

def main():
	nums = ["", ""]
	for i in range(2):
		while True:
			isNegative = False
			nums[i] = input("Please give a number to multiply: ")
			if (nums[i][0] == "-"):
				nums[i] = nums[i][1:]
				isNegative = True
			if (nums[i].isdigit()):
				nums[i] = int(nums[i])
				if (isNegative):
					nums[i] = -nums[i]
				break
			else: print("This is not a number!")
	if (nums[0] < 0 and nums[1] < 0):
		nums[0] = -nums[0]
		nums[1] = -nums[1]
	elif (nums[0] > 0 and nums[1] < 0):
		transfNum = nums[0]
		nums[0] = nums[1]
		nums[1] = transfNum
	mult(nums)
	again()
main()
