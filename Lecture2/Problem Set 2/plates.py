def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lenght(s) and check_beginning(s) and check_num_zero(s) and check_punctuation(s):
        return True
    else:
        return False

#ckecked
def lenght(s): # return False if the lenght is less than 2 or more than 6, returns True otherwise
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

#checked
def check_beginning(s): # if just one of the first two characters is a number, returns False, else returns True
    for i in s:
        if s[0].isdigit() == True or s[1].isdigit() == True:
            return False
        else:
            return True
    return

def check_num_zero(s): # check if numbers come before letters
    for char in s:
        if s.isalpha():
            return True
        elif char.isdigit():
            pos = s.index(char)

            if s[pos:].isdigit() and int(char) != 0:
                return True
            else:
                return False


def check_punctuation(s):
    for char in s:
        if char in [" ", ".", ",", "!", "?"]:
            return False
        else:
            return True

main()
