Count = 0
Total = 0

while True :
	Num = raw_input("Enter a number: ")
	if Num == 'Done' : break
	if Num < 1 : break
	try :
		Inp = float(Num)
	except :
		print "Invalid input"
		continue
  
	Count = Count + 1
	Total = Total + Inp	
	Average = Total/Count
	print Inp, Count, Total, Average
print Total, Average,'All Done'



