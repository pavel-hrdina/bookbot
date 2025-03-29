

def main() -> None:
    """
    Main method of the program.
    :return: None
    """
    # Check if the script received any arguments
    book_content = get_book_text('./books/frankenstein.txt')
    return length_of_string(book_content)


def get_book_text(filepath) -> str:
    """
    Takes a filepath and returns its content.
    :param filepath: str
    :return: str
    """
    with open(filepath) as f:
        return f.read()


def length_of_string(text: str) -> None:
    """
    Takes a string and returns its length.
    :param text: str
    :return: None
    """
    length = len(text.split())
    print(f"{length} words found in the document")


if __name__ == '__main__':
    main()

