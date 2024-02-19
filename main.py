def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = count_words_in_book(text)
    print(f"{count_of_words} words found in the document")
    count_of_letters = count_letters(text)
    print(count_of_letters)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words_in_book(book):
    return len(book.split())

def count_letters(book):
    letter_dict = {}
    book_list = list(book)
    for letter in book_list:
        lowercase_letter = letter.lower()
        if lowercase_letter not in letter_dict.keys():
            letter_dict[lowercase_letter] = 1
        else:
            letter_dict[lowercase_letter] += 1
    return letter_dict

main()