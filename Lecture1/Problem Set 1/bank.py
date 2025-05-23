# Implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


def main():
    greeting = input("Greeting: ").lstrip().capitalize()

    if (greeting.startswith("Hello") == True):
        print("$0")
        return
    elif (greeting.startswith("H") == True):
        print("$20")
        return
    else:
        print("$100")

main()
