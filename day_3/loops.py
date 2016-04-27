'''
a = [45,77,44,22,54,-56,34]

for i in range (len(a) -1, -1, -1):
	print i

#print in reverse

i = len (a)

while i > 0:
	print a [i -1]
	i -= 1 
'''


b = [(2, 4), (5,10), (6,20), (50,50)]

'''
 x: 2, y: 4
 x: 5, y: 10
''' 

for x  in b:
	print "x:{} , y:{}".format (*x)

c = [(2, 4,3), (5,10,5), (6,20,7), (50,50,87)]

for i in c:
	print "x: {}, y: {}, z: {}".format (*i)




