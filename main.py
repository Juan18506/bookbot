def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def get_chars_dict(text: str) -> dict[str]:
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    chars_dict = get_chars_dict(text)
    print(chars_dict)


main()
