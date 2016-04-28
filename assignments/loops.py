def looped(*args):

	
	for arg in args:
		res = "x: {}, y: {}".format(*arg)
		for a in arg:
			if len (a) == 2:
				res = "x: {}, y: {}".format(*a)
				
			else:
				res = "x: {}, y: {}, z: {} ".format(*a)
			print "I dont know whats happening"

	return res


				
				
					
print looped ([(10,20,30), (10,40),(4,5,50)])






