def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    count = count_words_in_book(text)
    print(count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words_in_book(book):
    return len(book.split())

main()