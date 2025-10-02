def add(x , y):
    return x + y

def subtract(x , y):
    return x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def power(x , y):
    return x ** y   

def modulus(x , y):
    return x % y    

def floor_divide(x , y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x // y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x ** 0.5

def factorial(n):
    if n < 0:
        raise ValueError("Cannot compute factorial of a negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole cannot be zero.")
    return (part / whole) * 100

def average(numbers):
    if not numbers:
        raise ValueError("The list of numbers cannot be empty.")
    return sum(numbers) / len(numbers)  

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a    

def lcm(a, b):
    if a == 0 or b == 0:
        raise ValueError("LCM is not defined for zero.")
    return abs(a * b) // gcd(a, b)

def main():
    print("Welcome to the Advanced Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Divide")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Percentage")
    print("11. Average")
    print("12. GCD")
    print("13. LCM")
    print("Enter 'e' to exit")


    while True:
        choice = input("Enter choice(1-13) or 'e' to exit: ")

        if choice == 'e':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in [str(i) for i in range(1, 14)]:
            try:
                if choice in ['1', '2', '3', '4', '5', '6', '7']:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        print(f"{num1} + {num2} = {add(num1, num2)}")
                    elif choice == '2':
                        print(f"{num1} - {num2} = {subtract(num1, num2)}")
                    elif choice == '3':
                        print(f"{num1} * {num2} = {multiply(num1, num2)}")
                    elif choice == '4':
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    elif choice == '5':
                        print(f"{num1} ^ {num2} = {power(num1, num2)}")
                    elif choice == '6':
                        print(f"{num1} % {num2} = {modulus(num1, num2)}")
                    elif choice == '7':
                        print(f"{num1} // {num2} = {floor_divide(num1, num2)}")

                elif choice == '8':
                    num = float(input("Enter number: "))
                    print(f"Square root of {num} = {square_root(num)}")

                elif choice == '9':
                    num = int(input("Enter a non-negative integer: "))
                    print(f"Factorial of {num} = {factorial(num)}")

                elif choice == '10':
                    part = float(input("Enter the part value: "))
                    whole = float(input("Enter the whole value: "))
                    print(f"Percentage: {percentage(part, whole)}%")

                elif choice == '11':
                    nums = input("Enter numbers separated by spaces: ")
                    num_list = list(map(float, nums.split()))
                    print(f"Average: {average(num_list)}")

                elif choice == '12':
                    num1 = int(input("Enter first integer: "))
                    num2 = int(input("Enter second integer: "))
                    print(f"GCD of {num1} and {num2} = {gcd(num1, num2)}")

                elif choice == '13':
                    num1 = int(input("Enter first integer: "))
                    num2 = int(input("Enter second integer: "))
                    print(f"LCM of {num1} and {num2} = {lcm(num1, num2)}")

            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()