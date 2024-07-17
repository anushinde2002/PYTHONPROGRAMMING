def factorial(x):
  fact=1
  for i in range(1,x+1):
    fact=fact*i
  print("factorial is",fact)
factorial(5)