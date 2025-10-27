input = "I love programming"
def get_split_word(input):
	words = []
	new_words = ""

	for char in input:
		if char == " ":
			words.append(new_words)
			new_words = ""
		else:
			new_words += char
	words.append(new_words)
	return words

print(get_split_word(input))