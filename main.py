import sys
from stats import num_words, num_characters, sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1] 

def get_book_text(path):   
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def main():
    text = get_book_text(path)
    word_count = num_words(text)
    char_count = num_characters(text)
    characters = num_characters(text)
    sorted_chars = sorted_list(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


if __name__ == "__main__":

	main()






