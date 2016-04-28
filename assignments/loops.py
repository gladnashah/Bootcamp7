def looped(*args):

	
	for arg in args:
		print arg
		for a in arg:
			print a
			if len (a) == arg:
				return "x: {}, y: {}".format(*a)
				
			else:
				return "x: {}, y: {}, z: {} ".format(*a)
				
				
		
			print "I dont know whats happening"
				
		

print looped ([(10,20,30), (10,40)], [(4,5,50)])






