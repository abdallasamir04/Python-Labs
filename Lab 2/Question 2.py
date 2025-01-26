def multiplication_table():
    while True:

        try:
            n = int(input("Enter a number to generate the multiplication table: "))
            if n <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


        table = [[i * j for j in range(1, i+1)] for i in range(1, n+1)]
        print("Multiplication Table:")
        for row in table:
            print(row)


        repeat = input("Do you want to generate another table? (yes/no): ").lower()
        if repeat != 'yes':
            print("Exiting the program. Goodbye!")
            break


multiplication_table()