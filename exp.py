import re

fhand = raw_input('enter the file name:')
fh = open(fhand)
for line in fh:
	line = line.rstrip()	
	if re.search('^From:',line) :	
		#print line

		
fhand = raw_input('enter the file name:')
fh = open(fhand)
for line in fh:
	line = line.rstrip()	
	if re.search('^X.*:',line) :	
		#print line
		
x = 'From cwen@iupui.edu Thu Jan  3 16:23:48 2008'
y = re.findall('\S@\S+',x)
print y