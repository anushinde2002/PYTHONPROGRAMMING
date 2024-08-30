import math
class Rectangle:
    def area(self):
        len = int(input("Enter length of Rectangle "))
        bre = int(input("Enter breadth of Rectangle "))
        print(f"The area of rectangle is {len * bre} ")
class Square:
    def area(self):
        sq_area = int(input("Enter number to find area of Square "))
        print(f"The area of square is {sq_area * sq_area}")
class Triangle:
    def area(self):
        h = int(input("Enter Height of triangle "))
        b = int(input("Enter base of triangle "))
        t_area = 1 / 2 * (h * b)
        print(f"The area of square is {t_area}")
class Circle:
    def area(self):
        r = int(input("Enter  radius of circle "))
        r_area = math.pi * (r * r)
        print(f"Area of circle is {r_area} ")

S=Square
r=Rectangle
c=Circle
t=Triangle
while(True):
        print("find Areas \nEnter 1 to find area of Square \n Enter 2 to find area of rectangle \n"
              " Enter 3 to find area of triangle \n Enter 4 to find area of circle \n Enter 0 to exit")
        n = int(input())
        match (n):
            case 1:
                S.area(2)
            case 2:
                r.area(3)

            case 3:
                c.area(4)
            case 4:
                t.area()

            case 0:
                print("Ok Bye bye")
                exit()
            case _:
                print("Enter above choices only")
