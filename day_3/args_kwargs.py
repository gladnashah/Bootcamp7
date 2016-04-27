def hello (name, age, class_=''):
	'''

	Explains
	'''
	if class_ != '':
		return "I am {}, and I am {} old and am {}".format (name, age, class_)

	return "I am {}, and I am {} old".format (name, age)


people = [
			("Jane", 23, "high"),
			("Joe", 25),
			("Brian", 60),
			("Betty", 45),
			]
#for name, age, class_ in people:
#	print hello (name, age, class_)

#use of unpacking
for person in people:
	print hello (*person)

def super_sum(a, b, *args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g. super_sum(10,20) = 30
		super_sum (10, 20, 40) = 70
		super_sum (1, 4, 5, 6, 7) = 23

	'''
	total = 0
	for i in args:
		total += i

	return total + a + b

print super_sum(10, 20)
print super_sum(10, 20, 40)
a = [10, 40, 60]
print super_sum (*a)
print super_sum (10, 20)

def hello_again (**kwargs):
	return "I am {}, and I am {} old".format (kwargs ['name'], kwargs ['age'])

print hello_again (name='Joe', age=20)
print hello_again (age=20, name='Jane')

other_people = [
		{'name': 'Joe', 'age': 98},
		{'name': 'Jane', 'age': 98},
		{'name': 'Trump', 'age': 98},
		]
joe = {'name': 'Joe', 'age': 98}

print hello_again (**joe)
print hello_again (name='joe', age= 98)


other_people = [
		{'name': 'Joe', 'age': 98},
		{'name': 'Jane', 'age': 98},
		{'name': 'Trump', 'age': 98},
		]
for person in other_people:
	hello_again (**person)




