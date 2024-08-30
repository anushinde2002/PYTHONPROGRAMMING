def area(shape,*dimensions):
    area_f ={
        'circle':lambda r:3.14*r*r,
        'square':lambda s:s**2,
        'rectangle':lambda l,w:l*w,
        'triangle': lambda h, b: 1.5*h*b
    }
    return area_f[shape](*dimensions)

shape = input("Enter name of the shape: ")
if(shape=='circle'):
    r=int(input("Enter radius: "))
    print("Area of Circle",area(shape,r))
elif(shape=='square'):
    s = int(input("Enter side: "))
    print("Area of Square",area(shape,s))
elif(shape=='rectangle'):
    l = int(input("Enter length: "))
    w = int(input("Enter width: "))
    print("Area of Rectangle",area(shape,l,w))
elif(shape=='triangle'):
    b = int(input("Enter height: "))
    h = int(input("Enter base: "))
    print("Area of Triangle", area(shape,h,b))
else:
    print("Enter valid shape")