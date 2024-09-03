#Decorators
#function decorator

import functools
# def start_end_decorator(func):
    
#     @functools
#     def wrapper():
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper


def repeat(num_time):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
      for _ in range(num_time):
        result = func(*args,**kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_time=5)
def greet(name):
  print(f"Hello {name}")


greet("Alex")




        
        

