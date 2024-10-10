# returning a value so function has got a value
def cube(num):
    return num * num * num


print(cube(7))  # 343


# different style
def cube(num):
    result = num * num * num
    return result


print(cube(2))  # 8


# IMPORTANT!!!
def cube(num):
    result = num * num * num
    return result
    print("code")  # this code is not working because after return statement


print(cube(3))  # 27

# NOTES
# we can return any data type like string, boolean, number
# if you wanna get a value from function you should use return
