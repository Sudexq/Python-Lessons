# https://www.w3schools.com/python/python_classes.asp

from Student_1 import Student

# from file import class

student1 = Student("Ali", "Business", 2.7, False) #object
student2 = Student("Ayse", "Art", 3.4, True) #object

print(student1.gpa)  # 2.7
print(student2.is_regularly)  # True
