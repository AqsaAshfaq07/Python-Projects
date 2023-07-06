import random
from hangman_words import word_list
from hangman_art import stages, logo

word = random.choice(word_list)

end_of_game = False
lives = 6

print(logo)

#Create blanks
blanks = []
for _ in range(len(word)):
  blanks += "_"

while not end_of_game:
  guess = input("Guess a letter: ").lower()

  # If the user repeats a letter !
  if guess in blanks:
    print(f"You've already guessed this letter! {guess}")

  #Check guessed letter
  for pos in range(len(word)):
    letter = word[pos]

    if letter == guess:
      blanks[pos] = letter

  # If user has entered incorrect letter
  if guess not in word:

    print(
      f"Your guessed letter {guess} is not in the word. You lose a life :(")

    lives -= 1
    if lives == 0:
      end_of_game = True
      print("YOU LOST.")

  #Join all the elements into a String.
  print(f"{' '.join(blanks)}")

  #Check if user has got all letters.
  if "_" not in blanks:
    end_of_game = True
    print("YOU WIN !")

  print(stages[lives])