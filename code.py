def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    amount = principal * ((1 + rate / 100) ** time)
    return amount - principal

def main():
    print("Welcome to the Interest Calculator!")
    print("1. Simple Interest")
    print("2. Compound Interest")
    
    choice = input("Choose interest type (1 or 2): ")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time period (in years): "))

    if choice == '1':
        interest = simple_interest(principal, rate, time)
        print("Simple Interest is:", interest)
    elif choice == '2':
        interest = compound_interest(principal, rate, time)
        print("Compound Interest is:", interest)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
