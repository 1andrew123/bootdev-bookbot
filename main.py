import stats, sys
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

def sort_on(items):
    return items["num"]

def main():
    """
    Main function to execute the script.
    """
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]  # Path to the book file
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count = stats.get_num_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = stats.count_characters(book_text)
    character_list = []
    for character in character_count:
        tmpDict = {}
        tmpDict["char"] = character
        tmpDict["num"] = character_count[character]
        character_list.append(tmpDict)
    character_list.sort(key=sort_on, reverse=True)
    for r in range(len(character_list)):
        if(character_list[r]['char'].isalpha()):
            obj = character_list[r]

            print(f"{obj["char"]}: {obj['num']} ")



if __name__ == "__main__":
    main()  # Execute the main function