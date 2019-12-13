import sys

class MyObject(object):

   def __init__(self):
      pass

   def examine(self):
      print(self)


class Wall(MyObject):

    def __init__(self):
        pass


o = Wall()

print(dir(o))
print(dir([]))
print(dir({}))
print(type(()))
print(type(object))
print(type(MyObject))
print(type(o))
print(type(sys))
print(id(sys))
print(id(o))
print(id(object))

#attr
def fun():
    pass
print(hasattr(fun, '__doc__')) #The hasattr() function checks if an object has an attribute
print(hasattr(fun, '__call__'))

print(getattr(object, '__doc__'))#The getattr() function returns the contents of an attribute if there are some.
print(getattr(fun, '__doc__'))

#instance
print(isinstance(o, MyObject))
print(isinstance(o, object))

#The issubclass() function checks if a specific class is a derived class of another class
print(issubclass(MyObject, Wall))
print(issubclass(Wall, MyObject))

# The __doc__ attribute gives some documentation about an object and the __name__ attribute holds the name of the object.

def noaction():
    '''A function, which does nothing'''
    pass


funcs = [noaction, len, str]

for i in funcs:
    print(i.__name__)
    print(i.__doc__)