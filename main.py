def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = count_characters(text) 
    print(f"{num_words} words found in the document")
    #print("\n")
    print_char_counts(char_count)
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

#Create an empty dictionary
#Go through each character in the input string
#Update the count of each character in the dictionary
def count_characters(text):

    char_count = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count

def print_char_counts(char_count):
    # Convert dictionary to list of tuples
    char_list = list(char_count.items())
    char_list.sort(key=lambda x: x[1], reverse=True)

    for character, count in char_list:
        if character.isalpha():
            print(f"The '{character.lower()}' character was found {count} times")

#This line calls the main function
if __name__ == "__main__":
    main()

