#Lambda Functions-small one line anonymous function 
#lambda arguments:expressions

# add10=lambda x: x=10
# print(add10(5))

# def add10_func(x):
#   return x*10

# mul=lambda x,y:x*y 
# print(mult(2,7))

# points2D=[(1,2),(3,6),(6,9),(5,10)]
# points2D_sorted=sorted(points2D,key=lambda x:x[1])


# print(points2D)
# print(points2D_sorted)

# a=[1,2,3,4,5]
# b=map (lambda x:x*2,a)
# print(list(b))
# c=[x*2 for x in a]
# print(c)

# a=[1,2,3,4,5]
# b=filter (lambda x:x%2==0,a)
# print(list(b))
# c=[x for x in a if x%2==0]
# print(c)

a=[1,2,3,4,5]
b=reduce (lambda x:a)
print(list(b))
c=[x for x in a]
print(c)
