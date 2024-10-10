# when we created a tuple we can't change later

coordinates = (4, 5)
# like index:  0  1

print(coordinates[0])  # 4
print(coordinates[1])  # 5

# for example if we wanna change coordinates[0]
# coordinates[0] = 10 #TypeError: 'tuple' object does not support item assignment

# NOTES
# coordinates = [4, 5] it is a list
# coordinates = (4, 5) it is a tuple

#we can do like this also;
dots = [(4, 5), (6, 7), (41, 45)]
print(dots[0]) #(4, 5)
