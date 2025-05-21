# implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
# whether inputted in uppercase or lowercase

def main():
    shorten()

def shorten():
    twttr = input("Input: ")
    vowels = ["a", "e", "i", "o", "u"]
    capital_vowels = ["A", "E", "I", "O", "U"]
    for letter in twttr:
        if letter in vowels or letter in capital_vowels:
            print(letter.replace(letter, ""), end="")
        else:
            print(letter, end="")

    print()

main()
