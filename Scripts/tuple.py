x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print y 
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print days[2]

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith("From ") :
       e = line.find(':')
	   
       f = line[e-2:e]
       #print f
       counts[f] = counts.get(f, 0) +1
       #print count
lst = list()
for key, val in counts.items():
	lst.append( (key, val) )

lst.sort()
for val, key in lst[:] :
	print val, key