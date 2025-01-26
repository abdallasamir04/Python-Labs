def names_to_dict():
    while True:

        names = input("Enter a list of names (comma-separated): ").split(",")
        names = [name.strip() for name in names]  # Remove extra spaces


        dictionary = {}
        for name in names:
            if name:
                key = name[0].lower()
                if key not in dictionary:
                    dictionary[key] = []
                dictionary[key].append(name)

        # Sort the dictionary by keys
        sorted_dict = {k: sorted(v) for k, v in sorted(dictionary.items())}


        print("Sorted Dictionary:")
        for key, value in sorted_dict.items():
            print(f"{key}: {value}")


        repeat = input("Do you want to perform another operation? (yes/no): ").lower()
        if repeat != 'yes':
            print("Exiting the program. Goodbye!")
            break


names_to_dict()