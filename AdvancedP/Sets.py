#unordered and mutable 

# A={"sun","mon","tue","wed","thur"}
# print(type(A))
# print(A)

# A.add(1)
# A.add(2)
# A.add(3)
# A.add(4)


# A.discard(2)
# A.pop()
# A.delete()

# for x in A:
#   print(x)

# even={1,2,3,4,5}
# odd={3,5,7,11,13}
# prime={2,3,5,7,9}

# u=odd.union(even)
# print(u)

# i=even.intersection(prime)
# print(i)

# diff=even.difference(prime)
# print(diff)

# s=even.symmetric_difference(odd)
# print(s)

C={1,2,3,4,5,6,7,8,9}
D={1,2,3,10,11,12}

C.update(D)
print(C)

D.difference_update(C)
print(D)

C.remove(4)
print(C)

C.symmetric_difference_update(D)
print(C)

print(C.issubset(D))
print(C.issuperset(D))
print(C.isdisjoint(D))

#Frozenset
a=frozenset([1,2,3,4])

print(a)