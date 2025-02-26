while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /) or 'exit' to quit: ")

    if operator.lower() == 'exit':
        print("Exiting the calculator.")
        break

    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator!"

    print(f"The result is: {result}\n")

    another_calculation = input("Do you want to perform another calculation? (yes / No): ")
    if another_calculation.lower() != 'yes':
        print("Closing the calculator. Goodbye!")
        break