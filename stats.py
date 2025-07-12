def word_count(file_contents):
    words_length = len(file_contents.split())
    return words_length

def symbol_counter(file_contents):
    individual_symbols = {}
    lower_case = file_contents.lower()

    # Iterate through each character in the input string
    for char in lower_case:
        # Increment the count for the current character in the dictionary
        individual_symbols[char] = individual_symbols.get(char, 0) + 1
        # The .get(char, 0) method retrieves the current count of the character.
        # If the character is not found, it returns 0 (its default value).
        # We then add 1 to this value and update the dictionary.

    return individual_symbols
