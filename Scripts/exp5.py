import re
 
content = open('actual.txt')
#numlist = list()
sum = 0
for line in content:
	numbers = re.findall('[0-9]+', line)
	#print max(len(numbers)
	#if len(numbers) > 0 : continue
	#count = count + 1
	#print count
	if len(numbers) > 0 : 
		for i in numbers:
			#numbers = int(newno)
			sum = sum + int(i)
print sum
	#num1 = int(numbers)
	#num2 = int(numbers[1])
	#numlist.append(num1)
	#numlist.append(num2)
#print numlist