def character_locator():
    while True:

        string = input("Enter a string: ")
        letter = input("Enter a letter to find: ")


        indices = [index for index, char in enumerate(string, start=1) if char.lower() == letter.lower()]


        if indices:
            print(f"The letter '{letter}' is found at positions: {indices}")
        else:
            print(f"The letter '{letter}' is not found in the string.")


        repeat = input("Do you want to perform another search? (yes/no): ").lower()
        if repeat != 'yes':
            print("Exiting the program. Goodbye!")
            break


character_locator()