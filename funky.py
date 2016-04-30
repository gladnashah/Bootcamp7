def funky(a, b):
	if type(a)== int and type (b)== int:
		return (a + b)
	elif type (a)== float and type (b)== float:
		return (a + b)
	elif type (a)== str and type (b)== str:
		return (a + b)
	elif type (a)== list and type (b)== list:
		return (a + b)
	elif type (a)== dict and type (b)== dict:
		dictionary = dict(a.items() + b.items())
		return dictionary
	else:
		print "NO CAN DO"

print funky(30888,6999)
print funky(3.1425, 6.899)
print funky('Mary ', 'Mutanu')
print funky ([1,2,3,4], [5,6,7,8])
print funky ( {'fname':'Mercy'}, {'lname': 'Wanja'})

