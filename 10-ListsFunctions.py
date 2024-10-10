numbers = [1, 2, 3, 4, 5, 6]
names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]

names.extend(numbers)
print(names)  # ['Ali', 'Ayse', 'Zeynep', 'Hasan', 'Derya', 1, 2, 3, 4, 5, 6]

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names.append("Esma")  # adding end of the list
print(names)  # ['Ali', 'Ayse', 'Zeynep', 'Hasan', 'Derya', 'Esma']

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
# index:  0       1        2         3        4

names.insert(1, "Yusuf")  # adding middle of the list
print(names)  # ['Ali', 'Yusuf', 'Ayse', 'Zeynep', 'Hasan', 'Derya']
# on index 1 is slide to right and then Yusuf is taking index 1

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names.remove("Hasan")
print(names)

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names.clear()  # clear everything
print(names)  # []

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names.pop()  # removing last element in the list
print(names)  # ['Ali', 'Ayse', 'Zeynep', 'Hasan']

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
print(names.index("Zeynep"))  # 2
print(names.index("Ali"))  # 0
# print(names.index("Deniz")) #ValueError: 'Deniz' is not in list

names = ["Ali", "Ayse", "Ayse", "Zeynep", "Hasan", "Derya"]
print(names.count("Ayse"))  # 2 #how many "Ayse"?

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names.sort()  # sorting alphabetical
print(names)  # ['Ali', 'Ayse', 'Derya', 'Hasan', 'Zeynep']

numbers = [1, 5, 2, 4, 3, 6]
numbers.sort()  # sorting little to big
print(numbers)  # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5, 6]
numbers.reverse()  # reversing order
print(numbers)  # [6, 5, 4, 3, 2, 1]

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names2 = names.copy()  # copy list!
print(names2)  # ['Ali', 'Ayse', 'Zeynep', 'Hasan', 'Derya']
