def main():
    #list of Definitions
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = word_count(file_contents)
    individual_symbols = symbol_counter(file_contents)

    sorted_final = organized_list(individual_symbols,)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char_dict in sorted_final:
        print(f"{char_dict['char']}: {char_dict['num']}")

    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
    return (book)

from stats import word_count, symbol_counter, organized_list



main()
