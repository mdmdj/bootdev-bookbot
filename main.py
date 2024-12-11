def main():
    #Open and Read File
    book_file_path = "books/frankenstein.txt"
    book_text = get_book_text_from_file_path(book_file_path)
    
    #Process File
    word_count = get_word_count_from_text(book_text)
    count_dictionary = get_unique_character_counts_from_text(book_text)
    count_list = get_list_from_dictionary(count_dictionary)
    count_list.sort(reverse=True, key=sort_on_count)

    #Print Report
    print_report(book_file_path,word_count,count_list)

def print_report(path,word_count,count_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print("")
    print_character_count_list(count_list)


def get_book_text_from_file_path(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count_from_text(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_unique_character_counts_from_text(text):
    text_normalized = text.lower()

    count_dictionary = {}

    for c in text_normalized:
        if c not in count_dictionary:
            count_dictionary[c] = 0
            #print(f"adding {c} to dictionary")
        
        #print(f"incrementing {c}")
        count_dictionary[c] = count_dictionary[c] + 1
        #print(f"{c} is now {count_dictionary[c]}")

    return count_dictionary

def get_list_from_dictionary(dict):
    list = []

    for k in dict:
        list.append({"character":k,"count":dict[k]})

    return list 

def sort_on_count(dict):
    return dict["count"]

def print_character_count_list(list):

    for v in list:
        c = v["character"]
        count = v["count"]
        if c.isalpha():
            print(f"The '{c}' character was found {count} times")

main()