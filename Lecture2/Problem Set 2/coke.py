def main():
    cents_sum = 0
    due = 50
    while due > 0:
        cents = int(input("Insert Coin: "))
        if cents in [25, 10, 5]:
            cents_sum = cents_sum + cents
            due = 50 - cents_sum
        else:
            print(f"Amount Due: {due}")
        if due > 0:
            print(f"Amount Due: {due}")
        else:
            break

    change = cents_sum - 50
    print(f"Change Owed: {change}")

main()
