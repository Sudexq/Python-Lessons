# 2D Lists
numbers = [
    # 0 1  2
    [1, 2, 3],  # 0
    [4, 5, 6],  # 1
    [7, 8, 9],  # 2
]
print(numbers[2][1])  # 8
print(numbers[0][0])  # 1
print(numbers[1][1])  # 5
print(numbers[2][2])  # 9

#Nested Loops

for row in numbers:
    for col in row:
        print(col)

"""
1
2
3
4
5
6
7
8
9
"""