# our identifier is def

def say_hi():
    print("Hello User")  # there is must be space at start of the line
#if there is no space then you are outside of the function

#calling function;
say_hi() #Hello User


#FUNCTION WITH ONE PARAMETER

def say_hi(name):
    print("Hello " + name)

say_hi("Azra") #Hello Azra

#FUNCTION WITH MORE THAN ONE PARAMETER

def say_hi(name, age):
    print("Hello "+ name + ", you are " + age+ " years old.")

say_hi("Ali", "20") #Hello Ali, you are 20 years old.

#INTEGER TO STRING
def say_hi(name, age):
    print("Hello "+ name + ", you are " + str(age)+ " years old.")

say_hi("Ali", 20) #Hello Ali, you are 20 years old.