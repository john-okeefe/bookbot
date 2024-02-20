def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_of_words = count_words_in_book(text)
    count_of_letters = count_letters(text)
    human_readable_letter_count = map(human_readable_letter_count_map, dict_sort_and_convert(count_of_letters))
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_of_words} words found in the document")
    print("\n")
    for sentence in list(human_readable_letter_count):
        print(sentence)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words_in_book(book):
    return len(book.split())

def count_letters(book):
    letter_dict = {}
    for letter in book:
        lowercase_letter = letter.lower()
        if lowercase_letter.isalpha() == True:
            if lowercase_letter not in letter_dict.keys():
                letter_dict[lowercase_letter] = 1
            else:
                letter_dict[lowercase_letter] += 1
    return letter_dict

def sort_on(dict):
    return dict["count"]

def dict_sort_and_convert(dict):
    dict_list = []
    for key in dict.keys():
        new_dict = {"letter": key, "count": dict[key]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def human_readable_letter_count_map(dict):
    return f"The '{dict["letter"]}' character was found {dict["count"]} times"

main()