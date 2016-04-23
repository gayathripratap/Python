
import re
 
content = open('actual.txt')
numlist = list()
 
for line in content:
	numbers = re.findall('[0-9]+', line)
	if len(numbers) == 2:
		num1 = int(numbers[1])
		numlist.append(num1)
	print numlist,
	sum = 0
	count = 0
	for number in numlist:

		count += 1
		sum = sum + number
	print count,sum