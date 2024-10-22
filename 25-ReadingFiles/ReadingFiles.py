# "r" reading file
# "w" overwrite any existing content
# "a" append to the end of the file
# "x" Creates the specified file, returns an error if the file exists

# "t" Default value. Text mode
# "b" Binary mode (e.g. images)

"""
file = open("TextFile.txt")
file = open("TextFile.txt", "r")
file = open("TextFile.txt", "rt")
#this all codes are same thing
#Because "r" for read, and "t" for text are the default values
"""

file = open("TextFile.txt", "r")
# print(file.read())  # reading the content of the file
# print(file.read(5)) # Return the 5 first characters of the file
# print(file.readline())  # Read first one line of the file
# print(file.readline())  # Read second one line of the file because there are two readline()

# print(file.readlines())
"""
['Hello! Welcome to TextFile.txt\n', 'This file is for testing purposes.\n', 'Good Luck!']
"""

# print(file.readlines()[1]) #output: This file is for testing purposes.


for line in file.readlines():
    print(line)

"""
Hello! Welcome to TextFile.txt

This file is for testing purposes.

Good Luck!
"""
# It is a good practice to always close the file when you are done with it.
file.close()
