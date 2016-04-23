largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9, 41, 12, 3, 74, 15] :
	if the_num > largest_so_far :
		largest_so_far = the_num
	print largest_so_far, the_num
print 'After', largest_so_far

x = -1
print 'Before', x
for i in [9, 41, 12, 3, 74, 15] :
	if i > x:
		x = i
	print x, i
print 'After', x

# counting Numbers

zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15] :
	zork = zork + 1
	print zork, thing
print 'After', zork

# summation of numbers
zork = 0
print 'Before', zork
for thing in [9, 41, 12, 3, 74, 15] :
	zork = zork + thing
	print zork, thing
print 'After', zork

# Average og numbers
count = 0
sum = 0
print 'Before', count, sum 
for thing in [9, 41, 12, 3, 74, 15] :
	count = count + 1 
	sum = sum + thing
	print count, sum 
print 'After', count, sum, sum/count

#filtering

for value in [12, 34, 56, 78, 98, 76] :
	if value > 50 :
		print 'Largest Number:', value
print 'done'

#searching

found = False
print 'Before', found
for value in [9, 41, 12, 3, 74, 15] :
	if value == 3 :
		found = True
	print found, value
print 'After', found

#smallest

largest_so_far = -1
print 'Before', largest_so_far
for the_num in [9, 41, 12, 3, 74, 15] :
	if the_num < largest_so_far :
		largest_so_far = the_num
	print largest_so_far, the_num
print 'After', largest_so_far

#smallest value
smallest = None
print 'Before'
for value in [2, 43, 4, 6, 1, 73, 19, 0] :
	if smallest is None :
		smallest = value
	elif  value < smallest	:
		smallest = value
	print smallest, value
print 'after', smallest
