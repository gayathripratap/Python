gpratap = open('strings.py')

count = 0 
for line in gpratap :
  count = count + 1
print count
gpratap = open('strings.py')
print gpratap.read()
#gpratap = open('strings.py')
#inp = str(raw_input("Print the program:"))
#if inp == 'yes' :
 # print gpratap.read()
#else :
#  print 'Done'
  
gpratap = open('strings.py')
inp = gpratap.read()
print 'Len',len(inp)
print inp[:25]

fname = raw_input('Enter the file name:')
#gpratap = open(fname)

try:
	fhand = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
count = 0
for line in fhand :
	line = line.rstrip()
	if not line.startswith('print'):
		count = count +1
		#print line, count
	#else :
		#print 'None'
print count