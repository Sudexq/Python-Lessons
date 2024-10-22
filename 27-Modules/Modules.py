"""
import mymodule #imported module

#we use function in module
mymodule.say_name("Ayse") #Hello, Ayse

age = mymodule.person1["age"]
print(age) #36
"""

"""
#Create an alias for mymodule called mx
import mymodule as mx

age = mx.person1["age"]
print(age) #36
"""

"""
# https://docs.python.org/3.13/py-modindex.html
# we can reach all built-in modules with this link

# There are several built-in modules in Python, which you can import whenever you like.
# External Libraries / Lib
import platform

x = platform.system()
print(x)  # Windows
"""

"""
#List all the defined names or function belonging to the platform module:
import platform

x = dir(platform)
print(x)
"""

#Import only the person1 dictionary from the module:
from mymodule import person1

print (person1["age"]) #36
#not mymodule.person1["age"], directly person1["age"]