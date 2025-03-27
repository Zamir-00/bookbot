from stats import count_words
from stats import count_characters
from stats import sort_dicts
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    path_to_book = sys.argv[1]
    print(count_words(get_book_text(path_to_book)))
    sorted_list = sort_dicts(count_characters(get_book_text(path_to_book)))
    for dict in sorted_list:
        if dict["character"].isalpha():
            print(f"{dict["character"]}: {dict["count"]}")
main()