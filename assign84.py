#fname = raw_input("Enter the file name:")
#fn = open(fname)
#lst = list()
#for line in fn:
	#a = line.split('.')
	#b = a.append(range(line))
	#a.append()
	#abc = line(0)+line(1)
	#n=range(len(a))
	#print append(line)
	
fname = raw_input("Enter file name: ")
fh = open(fname)

lst = list()
for line in fh:
    abc = line.split()

    for word in abc:
        if word in lst: continue
        else:
            lst.append(word)
print sorted(lst)
	