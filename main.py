from stats import get_num_words
def get_book_text(path):
    """
    Reads the content of a book from a file and returns it as a string.
    
    Args:
        path (str): The path to the book file.
        
    Returns:
        str: The content of the book.
    """
    with open(path) as f:
        file_content = f.read()
    return file_content


def main():
    """
    Main function to execute the script.
    """
    book_path = "books/frankenstein.txt"  # Path to the book file
    book_text = get_book_text(book_path)
    #print(book_text)  # Print the content of the book
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document.")
if __name__ == "__main__":
    main()  # Execute the main function