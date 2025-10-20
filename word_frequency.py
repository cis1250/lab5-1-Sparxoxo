#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)import string

import re

def get_sentence():
    """Ask the user to enter a valid sentence."""
    while True:
        sentence = input("Enter a sentence: ")

        if sentence and sentence[0].isupper() and sentence[-1] in ".!?":
            return sentence
        else:
            print("Please start with a capital letter and end with a period, question mark, or exclamation point.")


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


def main():
    sentence = get_sentence()
    words, freqs = calculate_frequencies(sentence)
    print_frequencies(words, freqs)


if __name__ == "__main__":
    main()
