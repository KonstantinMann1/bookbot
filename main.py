import sys
from stats import count_words, count_character

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    character_dict = count_character(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words")
    print("--------- Character Count -------")
    for value in character_dict:
        char = value["char"]
        num = value["num"]
        print(f"{char}: {num}")
    print("============= END ===============")

main()