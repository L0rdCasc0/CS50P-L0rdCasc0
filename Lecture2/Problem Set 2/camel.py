# camel.py
# implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case

def main():
    snakecase_convert()

def snakecase_convert():
    camel_case = input("camelCase: ").strip()
    for letter in camel_case:
        if letter.islower(): # we check if a letter is lowercase and print it as is if it is
            print(letter, end="")
        else:  # every uppercase letter is substituted by _"letter", so by itself but lowercase
            print("_" + letter.lower(), end="")  # the end have to be specified in order not to print a new line after every single letter check
    print()


main()

