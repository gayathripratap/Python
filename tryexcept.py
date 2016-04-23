x = raw_input('Enter Hours:')
y = raw_input('Enter Rate:')

try:
	Hours = int(x)
	#Rate = str(y)
except:
	Hours = -1
	#Rate = -1
print "Error,please enter numeric input"
if Hours or rate > 0:
	print "Enter Hours:",Hours
	print "Enter Rate:",Rate
elif Hours == str(x):
	print "Error,please enter numeric input"
	#if Hours > 0:
		#y = raw_input('Enter Rate:')
	#try:
		#Rate = int(y)
	#except:
		#Rate = -1
		#if Hours > 0:
			#print "Enter Rate:",Rate
		#else:
			#print "Error,please enter numeric input"