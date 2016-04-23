
# -*- coding: UTF-8 -*-
import re

fname = raw_input('Enter the file name;')
fh = open(fname)
numlist = list()
for line in fh:
	line= line.rstrip()
	abc = re.findall('[0-9]+', line)
	if len(abc) == 1 : 
		num1 = int(abc[0])
		numlist.append(num1)
	if len(abc) == 2 :
		num2 = int(abc[0])
		num2 = int(abc[1]
	    numlist.append(num2)
		numlist.append(num2)
	if len(abc) == 3 :
		#len(abc) == 3 :
		num3 = int(abc[0])
		num4 = int(abc[1]
		num5 = int(abc[2])
		numlist.append(num3)
		numlist.append(num4)
		numlist.append(num5) 
	#num2 = int(abc[2])
	#numlist.append(num)
	#numlist.append(num1)
	#numlist.append(abc)
#sum = 0
count = 0
for number in numlist :
	#sum = sum + number 
	count = count + 1
	
print numlist,count

for line in fh:
    abc = line.split()

    for word in abc:
        if word in lst: continue
        else:
            lst.append(word)