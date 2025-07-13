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


def sort_on(item):
    return item["num"]


def organized_list(individual_symbols):
        char_list = [{"char": key, "num": value} for key, value in individual_symbols.items() if key.isalpha()]
        char_list.sort(reverse=True, key=sort_on)

        return char_list


#Add a new function to your stats.py file that takes the dictionary of
# characters and their counts and returns a sorted list of dictionaries.
#Each dictionary should have two key-value pairs: one for the character
# itself and one for that character's count (e.g. {"char": "b", "num": 4868}).
#The .sort() method will be helpful here (see the example).
#Import and call the function in main.py, and capture the result.
#Print the report to the console as shown above.
#  If the character is not an alphabetical character (using the .isalpha() method),
#  just skip it.
