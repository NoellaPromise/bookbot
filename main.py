import sys
from stats import count_words, count_characters, sort_character_counts

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")
    char_counts = count_characters(book_text)
    sorted_chars = sort_character_counts(char_counts)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

main()