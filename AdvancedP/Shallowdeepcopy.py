#Shallow vs Deep copy
#variable with same reference
#shallow copy-> one level deep,only reference of nested child only
#deep copy-> full independent cpy

import copy
# org=[5,7,9,7,4]
# cpy=org
# cpy=6
# print(cpy)
# print(org)

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

class Company:
  def __init__(self,boss,employee):
    self.boss
    self.employee
p1=Person('Alex',55)
p2=Person('Joe',22)

company=Company(p1,p2)
company_clone=copy.deepcopy(company)
company_clone.boss.age=56
print(company_clone.boss.age)
print(company.boss.age)