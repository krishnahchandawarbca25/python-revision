def temperature():
    print("Choose your conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter your choice ( 1 or 2): ")
    if choice == "1":
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    elif choice == "2":
        fahrenheit = float(input("Enter the temperature in Fahrenheit:"))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")

temperature()
