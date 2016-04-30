def data_type(x):
	'''
	Takes in an argument, x:
		- For an integer, return x ** 2
		- For a float, return x / 2
		- For a string, return "hello" + x
		- For a boolean, return "boolean"
		- For a long, return squareroot (x ** 0.5)
	'''
	

	if type (x) == int:
		return x ** 2

	elif type (x) == float:
		return x / 2

	elif type (x) == str:
		return "Hello {}". format (x)

	elif type (x) == bool:
		return "Boolean"

	elif type (x) == long:
		return "Long"
	else:
		print "Invalid data type"


print data_type (2)
print data_type (3.14)
print data_type ("World")
print data_type (True)
print data_type (35 ** 45)
print data_type ([1,2,2])