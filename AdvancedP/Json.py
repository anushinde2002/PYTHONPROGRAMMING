import json



# person={
#   "firstname":"Anita",
#   "lastname":"Shinde",
#   "age":22,

# }
# personJSON=json.dumps(person,indent=4,separators=('; ','='))
# print(personJSON)

# with open('person.json','w') as file:
#   json.dump(person,file,indent=4)


class User:
  def __init__(self,name,age):
    self.name=name
    self.age=age
uer=User('Max',22)

def encode_user(e):
  if isinstance(o,User):
    return {'name':o.name,'age':o.age,o.__class__.__name__:True}
  else:
    raise TypeError('Object of type user is not JSON serializable')
  
from json import JSONEncoder
class UserEncoder(JSONEncoder):

  def default(self,o):
    if isinstance(o.User):
      return {'name':o.name,'age':o.age,o.__class__.__name__:True}
    return JSONEncoder.default(self,o)
  
userJSON=UserEncoder().encode(User)
print(userJSON)

def decode_user(dct):
  if User.__name__ in dct:
    return User(name=dct['name'],age=dct['age'])
  return dct 


user=json.loads(userJSON,object_hook=decode_user)
print(type(user))

print(user.name)


  