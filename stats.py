from collections import Counter

# Counts the number of words in the book text.
def count_words(book_text):
    word_list = book_text.split()

    return len(word_list)


# Counts the frequency of each character in the book text.
def count_characters(book_text):
    return Counter(book_text.lower())
    

    
# # Returns the value at index 1 of each tuple, which is used as the sorting key.
def sort_on(pair):
    return pair[1]
    

    
# Takes dict of chars and returns sorted list of chars.
def chars_dict_to_sorted_list(char_counts):
    char_list = list(char_counts.items())

    return sorted(char_list, reverse=True, key=sort_on)

   



