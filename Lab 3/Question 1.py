import math

def calculate_area():
    while True:
        # Ask the user for input
        shape = input("Enter the shape (t for triangle, r for rectangle, s for square, c for circle): ").lower()

        if shape == 't':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area}")
        elif shape == 'r':
            width = float(input("Enter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))
            area = width * height
            print(f"The area of the rectangle is: {area}")
        elif shape == 's':
            side = float(input("Enter the side of the square: "))
            area = side * side
            print(f"The area of the square is: {area}")
        elif shape == 'c':
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * (radius ** 2)
            print(f"The area of the circle is: {area:.2f}")
        else:
            print("Invalid shape. Please try again.")
            continue

        # Ask the user if they want to perform another calculation
        repeat = input("Do you want to calculate another area? (yes/no): ").lower()
        if repeat != 'yes':
            print("Exiting the program. Goodbye!")
            break

# Run the function
calculate_area()