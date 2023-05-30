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

def sort_list_key(char: dict) -> int:
    return char["num"]

def char_dict_to_sorted_list(chars_dict: dict) -> list:
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "num": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_list_key)
    return sorted_list

def get_book_report(path) -> None:
    text = get_book_text(path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = char_dict_to_sorted_list(chars_dict)
    
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    for char_dict in chars_sorted_list:
        char = char_dict["char"]
        num = char_dict["num"]
        if char.isalpha():
            print(f"The '{char}' character was found {num} times")
            
    print("--- End report ---")


def main():
    book_path = "books/frankenstein.txt"
    get_book_report(book_path)


main()
