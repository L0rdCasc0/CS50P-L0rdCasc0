# implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes
# if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

def main():
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

    if (answer == "42" or answer == "forty-two" or answer == "forty two"):
        print("Yes")
        return
    else:
        print("No")
        return

main()

