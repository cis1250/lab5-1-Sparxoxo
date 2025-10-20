#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)import string
# 1 Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies.

import re
import string
        
def get_sentence():
    """Ask the user to enter a valid sentence."""
    
    sentence = input("Enter a sentence: ")

    while not is_sentence(sentence):
        sentence = input("Invalid: Please start with a capital letter and end with a period, question mark, or exclamation point: ")
    return sentence

def calculate_frequencies(sentence):
    """Count how many times each word appears."""
    words = []
    freqs = []
    for token in sentence.split():
        word = token.strip(string.punctuation).lower()
        if word == "":
            continue

        if word in words:
            index = words.index(word)
            freqs[index] += 1
        else:
            words.append(word)
            freqs.append(1)
    return words, freqs


def print_frequencies(words, freqs):
    """Show the word frequencies."""
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]}: {freqs[i]}")


def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True


def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)


if __name__ == "__main__":
    main()
