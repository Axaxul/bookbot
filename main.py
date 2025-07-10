def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    num_words = word_count(file_contents)
    print (f"{num_words} words found in the document")

def get_book_text(file_path):
    with open(file_path) as f:
        book = f.read()
    return (book)

def word_count(file_contents):
    words_length = len(file_contents.split())
    return words_length

main()
