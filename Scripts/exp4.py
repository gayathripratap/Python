
import re
 
content = open('actual.txt')
numlist = list()
 
for line in content:
	numbers = re.findall('[0-9]+', line)
	if len(numbers) == 1:
		num1 = int(numbers[0])
		numlist.append(num1)
	#print numlist,
	#sum = 0
	#count = 0
	#for number in numlist:

		#count += 1
		#sum = sum + number
	#print count,sum
	if len(numbers) == 2:
		num2 = int(numbers[0])
		num3 = int(numbers[1])
		numlist.append(num2)
		numlist.append(num3)
		#print numlist
	if len(numbers) == 3:
		num4 = int(numbers[0])
		num5 = int(numbers[1])
		num6 = int(numbers[2])
		numlist.append(num4)
		numlist.append(num5)
		numlist.append(num6)
		#print numlist
 
summ = 0 
count = 0
for number in numlist:
	summ += number
	count += 1
print numlist,count,summ