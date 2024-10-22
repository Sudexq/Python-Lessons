"""
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("invalid input")

# output:
# Enter a number: a
# invalid input

"""

"""

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except:
    print("invalid input")

# output: invalid input
#it is wrong because giving wrong because of 10/0, we can't divide with 0
#but looking like we entered a number so we can fix this situation

"""

"""
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")

#output: Divided by zero 
#now it is correct 
"""
try:
    value= 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #we can do like this also
    print(err)
except ValueError:
    print("invalid input")

#output: division by zero
#correct!