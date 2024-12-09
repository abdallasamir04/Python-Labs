def read(filepath, option):
    with open(filepath, 'r') as file:
        if option == "all":
            return file.read()
        elif option == "5":
            return file.read(5)
        elif option == "line":
            return file.readline()
        elif option == "lines":
            return file.readlines()
        else:
            raise ValueError("Invalid option for reading. Choose 'all', '5', 'line', or 'lines'.")

def write(filepath, content, option):
    with open(filepath, 'w') as file:
        if option == "write":
            file.write(content)
        elif option == "lines":
            if isinstance(content, list):
                file.writelines(content)
            else:
                raise ValueError("Content must be a list of strings for 'lines' option.")
        else:
            raise ValueError("Invalid option for writing. Choose 'write' or 'lines'.")

def append(filepath, newcontent, option):
    with open(filepath, 'a') as file:
        if option == "write":
            file.write(newcontent)
        elif option == "lines":
            if isinstance(newcontent, list):
                file.writelines(newcontent)
            else:
                raise ValueError("Content must be a list of strings for 'lines' option.")
        else:
            raise ValueError("Invalid option for appending. Choose 'write' or 'lines'.")
