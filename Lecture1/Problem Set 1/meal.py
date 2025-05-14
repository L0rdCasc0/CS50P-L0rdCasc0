def main():
    time = input("What time is it? ").strip()

    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
        return
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
        return
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")
        return
    else:
        return


def convert(time):
    hours, minutes = time.split(":")     # previously split with time.split(":")[0] and time.split(":")[-1] but this is more efficient
    time = float(hours) + (float(minutes) / 60)

    return(time)


if __name__ == "__main__":
    main()
