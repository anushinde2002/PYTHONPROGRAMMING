import math

def main():
    shape = input("Enter the shape (circle, rectangle, square): ").lower()

    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_area(shape, radius)
    elif shape == "rectangle":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = calculate_area(shape, length, width)
    elif shape == "square":
        side = float(input("Enter the side of the square: "))
        area = calculate_area(shape, side)
    else:
        area = "Invalid shape"

    print(f"The area of the {shape} is: {area}")

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def calculate_rectangle_area(length, width):
    return length * width

def calculate_square_area(side):
    return side ** 2

def calculate_area(shape, *args):
    area_calculators = {
        "circle": calculate_circle_area,
        "rectangle": calculate_rectangle_area,
        "square": calculate_square_area
    }

    if shape in area_calculators:
        return area_calculators[shape](*args)
    else:
        return "Invalid shape"

if __name__ == "__main__":
    main()



