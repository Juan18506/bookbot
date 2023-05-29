def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()
    
def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    print(f"Word count: {number_of_words}")
    
main()