from stats import get_num_words
import sys


def main():
    #args = sys.argv
    
    #if len(args) < 2:
    #    print("Usage: python3 main.py <path_to_book>")
    #    sys.exit(1)

    #book_path = args[1]
    book_path = "books/frankenstein.txt"
    book_title = get_book_title(book_path)

    text = get_book_text(book_path)
    words = split_to_words(text)

    num_of_words = get_num_words(words)

    dict_of_character_count = count_characters_dict(text)
    list_of_character_count = create_character_list(dict_of_character_count)

    character_report = build_character_report(list_of_character_count)

    print(f"{num_of_words} words found in the document.")
    print(character_report)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    


def get_book_title(path):
    book_name = path.replace("books/", "").replace(".txt", "").replace("_", " ")
    book_title = " ".join(word[0].upper() + word[1:] for word in book_name.split())
    return book_title



def split_to_words(text):
    texts = text.split()
    return texts



def count_characters_dict(text):
    char_dictionary = {}

    for char in text.lower():
        if char in char_dictionary:
            char_dictionary[char] += 1
        else:
            char_dictionary[char] = 1
    
    return char_dictionary



def create_character_list(character_count_dict):
    character_list = []

    for letter in character_count_dict:
        if letter.isalpha():
            character_list.append({"letter": letter, "num": character_count_dict[letter]})

    return character_list 

def sort_by_char(dict):
    return dict["letter"]


def build_character_report(character_list):
    character_list.sort(key=sort_by_char)

    character_report_list = []
    character_report = ""

    for char in character_list:
        character_report_list.append(f"Letter '{char["letter"]}' appeared {char["num"]} times.")

    character_report = "\n".join(character_report_list)
    
    return character_report





main()