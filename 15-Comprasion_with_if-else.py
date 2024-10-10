def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        result = num1
    elif num2 >= num1 and num2 >= num3:
        result = num2
    else:
        result = num3

    return result


print(max_num(2, 5, 5))  # 5
print(max_num(1, 2, 3))  # 3


