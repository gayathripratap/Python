hours = raw_input('Enter Hours:')
try:
	h = int(hours)
except:
	h = -1
if h > 0 :
	rate = raw_input('Enter Rate:')
try:
    r = int(rate)
except:
	r = -1
#else:
	print 'Error,please enter numeric input'