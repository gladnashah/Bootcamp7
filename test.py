def add(a, b):
	"""print out the sum of two numbers
	"""
	#import pdb; pdb.set_trace()
	if type(a)== int and type (b)== int:
		print (a + b)
	elif type (a)== float and type (b)== float:
		print (a + b)
	else:
		print "NO CAN DO"

add(1, 11)
add('name', 'name')
add (1, 'string')
add(2.7, 2.4)