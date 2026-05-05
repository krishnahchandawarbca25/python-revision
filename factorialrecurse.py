def factorial():
    num = int(input("Enter a number: "))
    if num < 0:
        print("Error: Negative numbers do not have factorials.")
    elif num == 0 or num > 0:
        result = 1
        for i in range(1, num + 1):
            result *= i
        print(f"The factorial of {num} is: {result}")
factorial()


