Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = int(raw_input('Please enter number 1-9:'))
Please enter number 1-9:123456789
>>> if 0 <= x <= 9:
	if 1 <= x <= 3:
		s = raw_input('Please enter string:')
		n = int(raw_input('Enter the degree to which you want to build number:'))
		# perform a cycle of repetition lina n times
		i = 0
		while i < n:
			print s
			i+=1
	if 4 <= x <= 6:
		m = int(raw_input('Enter the degree to which you want to build number:'))
		# realize the construction of a number x in degree m
		print x ** m
	if 7 <= x <= 9:
		# perform the larger number x per unit time in the cycle 10,
		# at the same time on the screen to bring all 10 numbers
		i = 0
		while i < 10:
			x+=1
			print x
			i+=1

			
>>> else:
	
SyntaxError: invalid syntax
>>>     print 'Input Error'
    
  File "<pyshell#24>", line 2
    print 'Input Error'
    ^
IndentationError: unexpected indent
>>> 
