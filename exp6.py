import re
fname = raw_input('Enter the file name;')
fh = open(fname)
numlist = list()

for line in fh:
	line= line.rstrip()
	abc = re.findall('[0-9]+', line)
	if len(abc)< 1 : continue
	num2 = int(abc[0])
	numlist.append(num2)
	if len(abc)< 2 : continue
	num3 = int(abc[1])
	numlist.append(num3)
	#numlist.append(num1)
	#numlist.append(abc)
	if len(abc)< 3 : continue
	num4 = int(abc[2])
	numlist.append(num4)
sum = 0
count = 0
for number in numlist :
	sum = sum + number 
	count = count + 1
print count,numlist,sum