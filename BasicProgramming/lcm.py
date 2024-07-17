def lcm(a,b):
  lcm=0
  greater=0
  if(a>b):
    greater=a
  else:
    greater=b
  while(True):
    if(greater%a==0)and(greater%b==0):
      lcm=greater
      break
    greater+=1
    return lcm
lcm(15,25)
