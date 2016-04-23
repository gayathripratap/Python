

#x = raw_input('Enter the num:')
#i = 0
#print 'Before', x
#While True:
	#if i > x:
	#	x = i
	#print x, i
#print 'After', x

largest = None
smallest = None

while True :
	Num = raw_input("Enter a number: ")
	if Num == 'Done' : break
	if Num < 1 : break
	try :
		Inp = int(Num)
	except :
		print "Invalid input"
	else :
		if smallest is None:
			smallest = Inp
			largest = Inp
		elif Inp < smallest :
			smallest = Inp
		elif Inp > largest :
			largest = Inp
			
print smallest,largest