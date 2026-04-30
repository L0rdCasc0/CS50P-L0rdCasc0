def main():
    fraction = input("Fraction x/y: ")

    while check_fraction(fraction) == False:
        fraction = input("Please use a valid fraction: ")

    percent_convert(fraction)
def check_fraction(fraction):
    if not '/' in fraction:  # if the fraction isn't formatted properly we refuse the input
        return False

    if '.' in fraction:
        return False

    try:
        x, y = fraction.split("/")  # we split the fraction and turn the num and denum into floats
        x = float(x)
        y = float(y)
    except ValueError:  # if it isn't possible to turn the fraction into a float it means that the input can't be accepted
        return False

    if x > y or y == 0:  # we check for the last conditions, fraction < 1 and y != 0
        return False

def percent_convert(fraction):
    x, y = fraction.split("/")
    x = float(x)
    y = float(y)

    try:
        percent = round((x / y) * 100)
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
    except ZeroDivisionError:
        print("You can't divide by 0")

main()
