secret_word = "zaman"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True #if it is true there is no chance to win

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You Win!")

""" sample output:
Enter guess: hayat
Enter guess: yaşam
Enter guess: yol
Out of Guesses, YOU LOSE!
"""

""" sample output:
Enter guess: hayat
Enter guess: yaşam
Enter guess: zaman
You Win!
"""
