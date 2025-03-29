import sys

from stats import (
    char_dic_to_sorted,
    count_word_occurrences,
    get_book_text,
    length_of_string,
)


def main() -> None:
    """
    Main method of the program.
    :return: None
    """
    # Check if the script received any arguments
    if len(sys.argv) > 1:
        book_content = get_book_text(sys.argv[1])
        word_occurrences = count_word_occurrences(book_content)
        new_char_list = char_dic_to_sorted(word_occurrences)

        length_of_string(book_content)
        for char in new_char_list:
            print(char)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == '__main__':
    main()

