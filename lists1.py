#x = str([ 1, 2, 99])
#print range(x)  

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
	print 'Happy New Year:', friend
for i in range(len(friends)) :
	friend = friends[i]
	print 'Happy New Year:', friend
	
listone = list()
listone.append(" Gayathri ")
listone.append(" Pratap ")
listone.append(" 2000 ")
print listone

x = (listone + friends)
x.sort()
print x

#'Gayathri' in friends
#2000 in listone

nums = [3, 41, 12, 9, 74, 15]
print len(nums)

print max(nums)
print min(nums)
print sum(nums)

print float(sum(nums)/len(nums))

numlist = list()
while True :
	inp = raw_input('Enter a number: ')
	if inp == 'done' : break
	value = float(inp)
	numlist.append(value)
average = sum(numlist) / len(numlist)
print numlist,'Average:', average

asd = "I love you Pratap"
x = asd.split()
print x[3]
for  i in x :
  print i,
  print len(i)
  #print i(2)
 
 
line = 'first;second;third'
thing = line.split()
print thing
print len(thing)
thing = line.split(';')
print thing
print len(thing)