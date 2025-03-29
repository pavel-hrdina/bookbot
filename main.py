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
    book_content = get_book_text('./books/frankenstein.txt')
    word_occurrences = count_word_occurrences(book_content)
    new_char_list = char_dic_to_sorted(word_occurrences)

    length_of_string(book_content)
    for char in new_char_list:
        print(char)


if __name__ == '__main__':
    main()

