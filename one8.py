# how to invoke function from outside
def outer():
  print("outer fun")

def inner():
   print("inner fun")
   return inner
result=outer()
print(type(inner))
inner()
inner()
