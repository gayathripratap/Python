lang = str(raw_input('Enter the Language:'))
def greet(lang):
	if lang == 'es':
		print 'Hola'
	elif lang == 'fr':
		print 'Bonjour'
	else:
		print 'Hello'
	return "Pratap"
print greet(lang), 'Reddy'