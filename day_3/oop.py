class Person:
	#class variable
	people_count = 0

	def __init__(self, name, age):
		#instance variable
		self.name = name
		self.age = age
		Person.people_count +=1

	def __repr__(self):
		return "<object: {}, {}>".format (self.name, self.age)

	def say_hello (self):
		return "Hello, i'm {} and {} y/o". format (self.name, self.age)


p = Person ('Joe', 23)
p1 = Person ('Jane', 23)
p2 = Person ('Mercy', 23)

print p.say_hello()

a = [('jane', 23), ('joe', 30), ('Jacob', 32), ('carol', 78), ('rehab', 56) ]
b = []

for name, age in a:
	person = Person (name, age)
	b.append (person)
print b

for person in b:
	print person.say_hello()

print Person.people_count
print p2.people_count

