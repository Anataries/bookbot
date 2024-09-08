def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = get_num_words(file_contents)
    print(f"This book has {num_words} words")
    
def get_num_words(file_contents):
    num_words = file_contents.split()
    return len(num_words)

#This line calls the main function
if __name__ == "__main__":
    main()

