def sum_digits(L):
	'''
	Takes a list A, and returns
	the sum of all the digits in the 
	list e.g. [10,30,45] should return
	1 + 0 + 4 + 5

	'''

	total = 0
	for l in L:
		B = str (l)
		for b in B:
			total += int (b)

	return total

print sum_digits ([10, 30, 45])


