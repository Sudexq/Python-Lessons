is_male = True
is_tall = False

if is_male:
    print("you are a male")
else:
    print("you are not a male")

# output # you are male

# OR OPERATOR
if is_male or is_tall:
    print("you are a male or tall or both")
else:
    print("You are neither male nor tall")

# output # you are a male or tall or both

# AND OPERATOR
if is_male and is_tall:
    print("you are a tall male")
else:
    print("You are either not male or not tall or both")

# output #You are either not male or not tall or both

# WITH ELIF
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not (is_male) and is_tall:
    print("you are a tall female")
else:
    print("You are a short female")

# output #you are a short male
