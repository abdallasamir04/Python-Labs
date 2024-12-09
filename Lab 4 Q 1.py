from myexperience import read, write, append, inserttodb, update, delete, select


def display_menu():
    print("\n--- Operations Menu ---")
    print("1. Write to a file")
    print("2. Read from a file")
    print("3. Append to a file")
    print("4. Insert data into the database")
    print("5. Update data in the database")
    print("6. Delete data from the database")
    print("7. Select data from the database")
    print("8. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            filepath = input("Enter the file path: ")
            content = input("Enter the content to write: ")
            option = input("Choose write option ('write' for single string or 'lines' for list): ")

            if option == "lines":
                content = content.split("\\n")

            try:
                write(filepath, content, option)
                print(f"Content written successfully to {filepath}.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            filepath = input("Enter the file path: ")
            option = input("Choose read option ('all', '5', 'line', 'lines'): ")

            try:
                content = read(filepath, option)
                print("\n--- File Content ---")
                if isinstance(content, list):
                    print("".join(content))
                else:
                    print(content)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            filepath = input("Enter the file path: ")
            newcontent = input("Enter the content to append: ")
            option = input("Choose append option ('write' for single string or 'lines' for list): ")

            if option == "lines":
                newcontent = newcontent.split("\\n")

            try:
                append(filepath, newcontent, option)
                print(f"Content appended successfully to {filepath}.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            query = input("Enter the INSERT query: ")
            parameters = input("Enter the parameters as a tuple (e.g., 'value1', 'value2'): ")
            try:
                inserttodb(query, eval(parameters))
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            query = input("Enter the UPDATE query: ")
            parameters = input("Enter the parameters as a tuple: ")
            try:
                update(query, eval(parameters))
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            query = input("Enter the DELETE query: ")
            parameters = input("Enter the parameters as a tuple: ")
            try:
                delete(query, eval(parameters))
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "7":
            query = input("Enter the SELECT query: ")
            parameters = input("Enter the parameters as a tuple (or leave empty for no parameters): ")
            try:
                if parameters:
                    results = select(query, eval(parameters))
                else:
                    results = select(query)
                print("\n--- Query Results ---")
                for row in results:
                    print(row)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "8":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
