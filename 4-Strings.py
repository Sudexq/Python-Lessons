print("She is happy")
#She is happy

print("She is\nhappy")
#She is
#happy

print("She is \"happy\" ")
#She is "happy"

phrase= "She is happy"

print(phrase)
#She is happy

print(phrase + " and suprised")
#She is happy and suprised

print(phrase.lower())
#she is happy

print(phrase.upper())
#SHE IS HAPPY

print(phrase.isupper()) #is it upper case?
#False

print(phrase.upper().isupper())
#True

print(len(phrase))
#12

print(phrase[0])
#S

#She is happy
#01234567891011

print(phrase[7])
#h

print(phrase.index("h"))
#1   #it is starting from left so first h's index is 1

print(phrase.replace("She", "He"))
#He is happy