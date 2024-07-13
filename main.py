# This calculator is used to find out how much each person should pay after a meal, tip included.

def main():
    print("Welcome to the tip calculator \n")
    bill = float(input("What was the total bill? \n$"))
    tip_percent = int(input("What tip percentage would you like to give? (ex. 10, 12, 15...) \n")) / 100
    final_bill = bill + (bill*tip_percent)
    people = int(input("How many people to split the bill? \n"))
    answer = (final_bill / people)

    print(f"Each person should pay: ${answer:,.2f}")


if __name__ == '__main__':
    main()
