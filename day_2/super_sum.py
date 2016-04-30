def super_sum(A):
	'''
	Takes a list A, and:
		- Halves every even number
		- Doubles every odd number
	Returns the sum of all.

	'''
	
	total = 0

	for a in A:
		if a % 2 ==0:
			total += (a / 2)
		else:
			total += (a * 2)

	return total
