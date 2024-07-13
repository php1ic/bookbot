import pathlib
import string


def get_book_text(book_file):
    with open(book_file) as f:
        return f.read()


def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    count = dict.fromkeys(string.ascii_lowercase, 0)
    for c in book_text.lower():
        if c.isalpha():
            count[c] += 1
    return count


def create_report(character_count):
    return dict(sorted(character_count.items(), key=lambda item: item[1], reverse=True))


def main():
    src_file_path = pathlib.Path(__file__).parent
    book = pathlib.Path(r"books/frankenstein.txt")

    book_file = src_file_path / book

    text = get_book_text(book_file)
    words = count_words(text)
    characters = count_characters(text)
    report = create_report(characters)

    print(f"--- Begin report of {book} -- ")
    print(f"{words} words found in the document\n")

    for c in report.items():
        print(f"The '{c[0]}' character was found {c[1]} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
