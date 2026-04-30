def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            date = input("").strip().title()
            if check(date) == True:
                if '/' in date: # if the date is in mm/dd/yyyy format, it will be split into its components and they will be checked for invalid dates
                    m, d, y = date.split("/")
                    if (int(m) > 0 and int(m) < 13) and (int(d) > 0 and int(d) < 32):
                        return m, d, y
                    else:
                        return ("Format Error")

                else:  # if input is in format "month day, year", it will be formatted into "month day year" and split into its components
                    date = date.replace(",", "")
                    m, d, y = date.split(" ")
                    try:  # we want the number of the month instead of its name
                        if m in months:
                            m = months.index(m)
                            m = m + 1
                            return m
                        else:
                            return ("Date Error")
                    except ValueError: # if the month isn't in the list we reject the input
                        pass

            else:
                pass
        except ValueError:
            pass

        print(y, f"{m:02}", f"{d:02}", sep="-")


def check(date):
    if '/' in date == False:
        return False
    elif ', ' in date == False:
        return False
    else:
        return True

main()
