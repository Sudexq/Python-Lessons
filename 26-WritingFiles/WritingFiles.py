"""
file = open("TextFile.txt", "a")
file.write("\nNow the file has more content!")
file.close()
"""
# if you wanna new line you should put \n to first of the new content
# and if you compile ur code more than once the file would be messed up

""" 
file = open("TextFile.txt", "w")
file.write("Now the file has more content!")
file.close()
"""
#if we do like this our whole text will be deleted because we overwrote with "w"
#and now our file has got: "Now the file has more content!" only this.

file = open("index.html", "w")
file.write("<p>This is HTML</p>") #we created a new file and it is HTML file
file.close()


