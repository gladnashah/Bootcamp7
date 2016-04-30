from person import Person
from kenyan import kenyan

#person.py
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

#kenyan.py

k = kenyan ('Anne', 23)

k.probe (False)

print "Is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()

print k.corrupt
