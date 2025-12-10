from stats import get_num_words, get_num_char, get_sorted_char
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    chars = get_num_char(book)
    sorted_chars = get_sorted_char(chars)
       
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")\

    for character in sorted_chars:
        print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")
    


main()
