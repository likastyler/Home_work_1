x = int(input('Please enter number 1-9:'))
if 1 <= x <= 3:
	s = raw_input('Please enter string:')
	n = int(raw_input('Enter the degree to which you want to build number:'))
	# perform a cycle of repetition lina n times
	for ggeps in range (n):
		print s
elif x <= 6:
	m = int(input('Enter the degree to which you want to build number:'))
	print x ** m
elif x <= 9:
	# perform the larger number x per unit time in the cycle 10,
	# at the same time on the screen to bring all 10 numbers
	for hheps in range (10):
		x+=1
		print x
else:
    print 'Input Error'
    
