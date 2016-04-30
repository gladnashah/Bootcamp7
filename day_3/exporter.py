#global vars / not good practice
people = [
	('joe', 78),
	('janet', 67),
	('Brian', 56),
	]


def super_sum (*args):
	return sum (args)

def hello_again (name, age):
	return "I am {} and am {} years old".format(name, age)

def max_min (A):
	'''
	Returns max value - min value
	e.g. [10, 20, -5, 6, 50, 8]

	'''
	#return max (A) - min (A)

	max_, min_ = A[0], A [0]

	for i in A:
		if i > max_:
			max_ = i
		if i < min_:
			min_ = i

	return max_ - min_

