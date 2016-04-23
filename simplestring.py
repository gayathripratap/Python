count = 0
fruit = raw_input('Enter fruit name:')
for letter in fruit :
	print letter,
	#if letter == 'a' :
		#count = count + 1
		#print count
print fruit[:3]
print fruit[4:]
print fruit[6:8]
a = 'pratap'
b = 'gayu'
c = a + ' ' + b
print c

'r' in a

name = 'GaYAthri'
x = name.lower()
print name,x, 'PRATap'.lower()
y = name.find('Y')
print y 
z = name.replace('thri', '3')
print z