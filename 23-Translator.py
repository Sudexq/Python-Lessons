"""We write a function that converts vowels to the letter g."""


def translate_to_g(word):
    new_word = ""
    for letter in word:
        if letter.lower() in "aeuio": #AEUIOaeuio
            if letter.lower() == letter:
                new_word = new_word + "g"  # if letter is lower case
            else:
                new_word = new_word + "G"  # or it is upper case
        else:
            new_word = new_word + letter

    return new_word


print(translate_to_g("makas"))  # mgkgs
print(translate_to_g("tarak"))  # tgrgk
print(translate_to_g("terlik"))  # tgrlgk
print(translate_to_g("water"))  # wgtgr

result = translate_to_g(input("Enter a word: "))
print("Translated version: " + result)

"""
Enter a word: water
Translated version: wgtgr
"""
