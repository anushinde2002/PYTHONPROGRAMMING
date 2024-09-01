#itertools:product, permutations, combinations,accumulate, groupby, and infinite operator

# from itertools import product
# a=[1,2]
# b=[3,4]
# prod=product(a,b,repeat=2)
# print(list(prod))

# from itertools import permutations
# a=[1,2,3,4]
# perm=permutations(a,2)
# print(list(perm))

# from itertools import combinations
# a=[1,2,3,4,5]
# comb=combinations(a,2)
# print(list(comb))

# from itertools import accumulate
# a=[1,2,3,4]
# accum=accumulate(a,func=max)
# print(a)
# print(list(accum))

# from itertools import groupby

# def smaller_than_3(x):
#   return x<3
# a=[1,2,3,4]
# grp_obj=groupby(a,key=lambda x: x<3)
# for key,value in grp_obj:
#   print(key,list(value))



# from itertools import count,cycle,repeat
# # for i in count(10):
# for i in count(a):
#   print(i)
#   if i==15:
#     break

# from itertools import count,cycle,repeat
# a=[1,2,3,4,5]
# for i in cycle(a):
#   print(i)
  
from itertools import count,cycle,repeat
a=[1,2,3,4,5]
for i in repeat(1,5):
  print(i)
  