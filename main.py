def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = word_count(file_contents)
    print (f"{num_words} words found in the document")
    symbols = symbol_counter(file_contents)
    print (f" This is the result of test: {symbols}")

def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
    return (book)

from stats import word_count, symbol_counter

main()
