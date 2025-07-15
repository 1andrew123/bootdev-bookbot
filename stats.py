def get_num_words(book_text):    
    return len(book_text.split())  # Split the text into words
    
def count_characters(book_text):
    """
    Counts the number of each character in the book text.
    
    Args:
        book_text (str): The content of the book.
        
    Returns:
        int: The number of characters in the book text.
    """
    dict_characters = {}
    for char in book_text:
        if char in dict_characters:
            dict_characters[char] += 1
        else:
            dict_characters[char] = 1
    return dict_characters # Return the dictionary of character counts