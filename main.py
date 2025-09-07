import sys
from stats import get_book_word_count
from stats import get_book_char_count
from stats import get_sorted_dic


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def print_book_stats(book_path):
    book_text = get_book_text(book_path)
    word_count = get_book_word_count(book_text)
    character_count = get_sorted_dic(get_book_char_count(book_text))
    bookbot_String = "\n".join([
        "============= BOOKBOT ============",
        f"Analyzing book found at {book_path}...",
        "----------- Word Count ----------",
        f"Found {word_count} total words",
        "--------- Character Count -------",
    ])

    print(bookbot_String)
    for item in character_count:
        if (item['char']).isalpha():
            print(f"{item['char']}: {item['num']}")

    print(" ============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Error:Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    print_book_stats(path_to_book)


if __name__ == "__main__":
    main()
