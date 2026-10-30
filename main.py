from stats import count_words, count_characters, chars_dict_to_sorted_list 
import sys


# Opens book text file and returns its contents.
def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        file_contents = f.read()

    return file_contents


# Prints final book report.
def print_report(book_path, word_count, sorted_count):

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char, count in sorted_count:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")
    

# Checks if book path argument is included and calls helper functions.
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    

    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_count = chars_dict_to_sorted_list(char_count)

    print_report(book_path, word_count, sorted_count)



if __name__ == "__main__":
    main()

