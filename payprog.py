x = int(raw_input('Enter the number of hours worked by an employee:'))
y = int(raw_input('Enter the rate paid to an employee for an hour:'))
if x <= 40:
 pay = x*y
 #print 'pay',pay
else: 
 pay = (40*y) + (float(1.5)*(x-40)*y)  
print pay