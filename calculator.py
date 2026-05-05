def calculator():
    num1=float(input("Enter first number"))
    num2=float(input("Enter second number"))
    operator=input("Enter operator")
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
        if num2==0:
            print("Error: number cant be divided by zero")
    else:
        print("Invalid operator")

calculator()