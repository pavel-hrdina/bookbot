def length_of_string(text: str) -> None:
    """
    Takes a string and returns its length.
    :param text: str
    :return: None
    """
    length = len(text.split())
    print(f"Found {length} total words")


def get_book_text(filepath) -> str:
    """
    Takes a filepath and returns its content.
    :param filepath: str
    :return: str
    """
    with open(filepath) as f:
        return f.read()


def count_word_occurrences(book_content: str) -> dict[str, int]:
    """
    Takes a book content and return all occurrences of each character with
    the number of occurrences, there should be no more than one time, that a
    character appears in the dictionary, never twice or more.
    :param book_content:
    :return: dict[str, int]
    """
    char_count = {}
    to_lowercase = book_content.lower()  # deal with uppercase letters
    for char in to_lowercase:
        if char in char_count:
            char_count[char] += 1  # if seen for the nth time
        else:
            char_count[char] = 1  # if seen for the first time
    return char_count


def char_dic_to_sorted(char_dic: dict[str, int]) -> list[str]:
    sorted_char_list = sorted(char_dic.items(), key=lambda x: x[1], reverse=True)  # OMG magik
    sorted_char_list = [f'{key}: {value}' for key, value in sorted_char_list if key.isalpha()]  # wtf
    # print(sorted_char_list)  # for debug
    return sorted_char_list
