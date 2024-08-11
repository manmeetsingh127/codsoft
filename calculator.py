# Arithmetic Calculator in Python

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    while True:
        print("Select an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        while True:
            choice = input("Enter your choice (1/2/3/4): ")
            if choice in ('1', '2', '3', '4'):
                break
            print("Invalid input. Please try again.")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))

        repeat = input("Do you want to repeat the calculation? (y/n): ")
        if repeat.lower() != 'y':
            break

if __name__ == "__main__":
    main()