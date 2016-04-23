
name = raw_input('Enter the name:')
print name 
x = int(name) - 100
print x

fruit = raw_input('Enter the fruit name:')
x = int(raw_input('Enter the number:'))
length = len(fruit)
print length
letter = fruit[1]
print letter

letter2 = fruit[x -1]
print letter2

fruit = raw_input('Enter the fruit name:')
index = 0
while index < len(fruit) :
	letter = fruit[index]
	print index, letter
	index = index + 1
fruit = raw_input('Enter the fruit name:')
for letter in fruit:
	print fruit