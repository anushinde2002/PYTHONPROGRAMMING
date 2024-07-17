def prime(n):
  f=0
  for i in range(2,n):
    if(n%i==0):
      f=1
    else:
      f=0
    if(f==0):
      print("no is prime")
    else:
      print("no is not prime")

      
      