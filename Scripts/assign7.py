# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
y = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
       e = line.find(' ')
	
       f = line[e:]
       #continue
       z = float(f)
       count = count + 1
       y = z + y 
       #y = y + line
       #print y/count
print 'Average spam confidence:', y/count
#print e
    #print line
#print "Done"
