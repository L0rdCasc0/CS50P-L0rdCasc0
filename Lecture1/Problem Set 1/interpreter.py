# Implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value
# formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z.

def main():
    math = input("Expression: ")
    x, y, z = math.split(" ")

    x = float(x)
    z = float(z)

    if (y == "+"):
        print(x + z)
        return
    elif (y == "-"):
        print(x - z)
        return
    elif (y == "*"):
        print(x * z)
        return
    elif (y == "/" and y != 0):
        print(x / z)
        return
    else:
        print("Please input a correct expression")

main()
