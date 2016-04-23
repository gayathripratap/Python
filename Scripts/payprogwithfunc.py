Hours = int(raw_input('Enter the number of hours worked by an employee:'))
Rate = float(raw_input('Enter the rate paid to an employee for an hour:'))
def computepay(Hours, Rate) :
    if Hours <= 40:
	pay = Hours * Rate
 #print 'pay',pay
    else: 
	pay = (40*Rate) + (float(1.5)*(Hours-40)*Rate)  
    return pay
print computepay(Hours, Rate)