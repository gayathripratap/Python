lang = str(raw_input('Enter the Language:'))
def greet(lang):
	if lang == 'es':
		return 'Hola'
	elif lang == 'fr':
		return 'Bonjour'
	else:
		return 'Hello'
print greet(lang), 'Pratap Reddy'