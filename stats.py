def num_words(text):
    words = text.split()
    return len(words)


def num_characters(text):
	characters = {}	
	lowercase = text.lower()


	for char in lowercase:
		if char in characters:
			characters[char] += 1
		else:
			characters[char] = 1
	
	return characters

def sorted_list(characters):
	list_of_dicts  = []
	
	for char, count  in characters.items():
		char_info = {"char": char, "num": count}
		list_of_dicts.append(char_info)

	def sort_on(dict):
		return dict["num"]

	list_of_dicts.sort(reverse=True, key=sort_on)

	return list_of_dicts
	
