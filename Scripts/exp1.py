import re

fhand = raw_input('enter the file name:')
fh = open(fhand)
for line in fh:
	line = line.rstrip()	
	if re.search('^X.*:',line) :	
		print line
print line

fhand = raw_input('enter the file name:')
fh = open(fhand)
for line in fh:
	line = line.rstrip()	
	if re.search('^X-Sieve*:',line) :	
		print line
print line

x= 'My 3 favourite numbers are 3, 9, 23'
y = re.findall('[0-9]+',x)
z = re.findall('[aeiou]+',x)
print y, z

a= 'From: Using the : character '
b = re.findall('^F.+:$c', a)
b = re.findall('^F.+?:', a)
print a
print b