#Errors and Exceptions

#value error
# a=5
# b=c 

# f=open('C:\Users\Admin\Desktop\AdvancedP\Dictionary.py')

#index error
# a=[1,2,3,4]
# a[5]
# print(a)


#keyerror
# mydict={"name":"Akshada","age":22,"city":"Pune"}
# mydict['marks']

# x=-5
# if x<0:
#   raise Exception('x should be positive')

#Assertion error
# x=2
# assert(x==0),'x is not positive'

#zero divide by error
# a=5/0


# try:
#   a=5/0
# except Exception as e:
#   print('an error occured')


try:
  a=5/0
  b=a*4
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
else:
  print("everything is fine")
finally:
  print("cleaning up...")