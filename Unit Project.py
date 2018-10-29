import random

def main():
    welcome = ["you have 10 attempts, good luck"]

    for line in welcome:
        print(line, sep='\n')



    play_again = True

    while play_again:


        words = ["hangman", "Bagpipes", "backpack", "Stubbs", "clothing",
                 "computer", "python", "program", "glasses", "science",
                 "sweatpants", "school", "greenwood", "clocks", "trump",
                 "algebra", "basketball", "knives", "ninjas", "sports"
                 ]

        chosen_word = random.choice(words).lower()
        player_guess = None #chooses word based on the list and adds the number of characters towards the number of dashes.
        guessed_letters = []
        word_guessed = []
        for letter in chosen_word:
            word_guessed.append("-")
        joined_word = None

        HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  | | 
|
--------
""")

        print(HANGMAN[0])
        attempts = len(HANGMAN) - 1


        while (attempts != 0 and "-" in word_guessed):
            print(("\nYou have {} attempts remaining").format(attempts))
            joined_word = "".join(word_guessed)
            print(joined_word)

            try:
                player_guess = str(input("\nSelect a letter between A-Z" + "\n> ")).lower()
            except:
                print("That is not valid input. Please try again.")
                continue
            else: #this prevents the user from entering any number that is not between a-z.
                if not player_guess.isalpha():
                    print("That is not a letter. Please try again.")#if you don't print a letter it prints "That is not a letter. Please try again"
                    continue
                elif len(player_guess) > 1:
                    print("That is more than one letter. Please try again.")#if you input more than one letter it prints "That is more than one letter. Please try again"
                    continue
                elif player_guess in guessed_letters:
                    print("You have already guessed that letter. Please try again.")#if you already inputed a letter it prints "You have already guessed that letter. Please try again"
                    continue
                else:
                    pass

            guessed_letters.append(player_guess)

            for letter in range(len(chosen_word)):
                if player_guess == chosen_word[letter]:
                    word_guessed[letter] = player_guess

            if player_guess not in chosen_word: #if the player does not choose the correct word then it prints a hangman sprite
                attempts -= 1
                print(HANGMAN[(len(HANGMAN) - 1) - attempts])

        if "-" not in word_guessed:
            print(("\nGood Job, Your word was {}").format(chosen_word)) #if there are not more "-" then it means you have won.
        else:
            print(("\nToo bad stoopid donut, The word was {}.").format(chosen_word)) #if you used all your attempts then you lose.

        print("\nDo you want to play again?")

        response = input("> ").lower()
        if response not in ("yes", "y"):
            play_again = False

if __name__ == "__main__":
    main()