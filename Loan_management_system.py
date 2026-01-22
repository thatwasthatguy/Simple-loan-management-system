def calculate_loan():
    amount = float(input("Enter loan amount: "))
    rate = float(input("Enter interest rate (%): "))
    interest = (amount * rate) / 100
    total = amount + interest
    print("Total repayment amount:", total)

def main():
    while True:
        print("1. Calculate Loan")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            calculate_loan()
        elif choice == "2":
            break
        else:
            print("Invalid option")

main()
