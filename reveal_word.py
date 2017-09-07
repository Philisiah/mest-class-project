"""Given a string of text with a hidden word, APPLE
Write a program to reveal the hidden word
"""
text = 'OACXOPCXOPCXOLCXOEC' #SAHGJSDEKHKJVHZAKJHSKUNMZBCRNXZMNCJKJHAJLDSK'
#words = ['ants', 'apple', 'search']



# if text.upper():
# 	text = list(text.lower())
# text = list(text)


# for word in words:
# 	new_word = list(word)
# 	match = []
# 	for char in new_word:
# 		if char in text:
# 			match.append(char)
# 	if ('').join(match) in words:
# 		print (('').join(match).upper())
# print  (text[1:len(text)-1: 3]),

results = '' 

for key, character in enumerate(text):
	if text[key - 1] == 'O' and text[key + 1] == 'C':
		results += character

print(results)