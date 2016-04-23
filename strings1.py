#fruit = 'banana'
index = 0
count = 0
fruit = raw_input('Enter the fruit name:')
for letter in fruit:
	if index < len(fruit) :
		letter = fruit[index]
		print  letter,
		index = index + 1		
#for letter in fruit :
	
	if letter == 'a':
		count = count + 1
	print count
		
	#print fruit