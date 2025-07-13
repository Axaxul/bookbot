# This function will take the output from file contents, break it into
# Individual strings, and then count the number of strings.
def word_count(file_contents):
    words_length = len(file_contents.split())
    return words_length

#make capital letters lowercase.  Break strings down to individual letters.
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

# Defines the variable for sorting.
def sort_on(item):
    return item["num"]


def organized_list(individual_symbols):
        char_list = [{"char": key, "num": value} for key, value in individual_symbols.items() if key.isalpha()]
        char_list.sort(reverse=True, key=sort_on)

        return char_list
