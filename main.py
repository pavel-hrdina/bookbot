def main():
    return get_book_text('./books/frankenstein.txt')


def get_book_text(filepath) -> str:
    with open(filepath) as f:
        return f.read()


if __name__ == '__main__':
    print(main())

