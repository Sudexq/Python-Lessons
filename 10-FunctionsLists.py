numbers = [1, 2, 3, 4, 5, 6]
names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]

names.extend(numbers)
print(names)  # ['Ali', 'Ayse', 'Zeynep', 'Hasan', 'Derya', 1, 2, 3, 4, 5, 6]

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
names.append("Esma")
print(names)  # ['Ali', 'Ayse', 'Zeynep', 'Hasan', 'Derya', 'Esma']

names = ["Ali", "Ayse", "Zeynep", "Hasan", "Derya"]
# index:  0       1        2         3        4

names.insert(1, "Yusuf")
print(names)  # ['Ali', 'Yusuf', 'Ayse', 'Zeynep', 'Hasan', 'Derya']
# on index 1 is slide to right and then Yusuf is taking index 1
