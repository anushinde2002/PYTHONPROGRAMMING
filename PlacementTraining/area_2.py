def area_of_circle():
    r=float(input("Please enter radius: "))
    return 3.14*r*r
def area_of_square():
    s=float(input("Please enter side: "))
    return s*s
def area_of_traingle():
    h=float(input("Please enter height: "))
    b=float(input("Please enter base: "))
    return 0.5*b*h
def area_of_rectangle():
    l=float(input("Please enter length: "))
    b=float(input("Please emter breadth: "))
    return l*b

print("1-area of circle")
print("2-area of square")
print("3-area of rectangle")
print("4-area of triangle")
ch=int(input("enter choice"))
if(ch==1):
    area = area_of_circle
    print(area())
elif(ch==2):
    area = area_of_square
    print(area())
elif(ch==3):
    area = area_of_rectangle
    print(area())
else:
    area = area_of_traingle
    print(area())

