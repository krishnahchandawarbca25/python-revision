def largestnumber():
    print("Enter three numbers: ")
    num1 = int(input("First number:"))
    num2 = int(input("Second number:"))
    num3 = int(input("Third number:"))
    if num1 >= num2 and num1 >= num3:
       largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:        largest = num3
    print("The largest number is:", largest)
largestnumber()
