Check this link to get related files and complete code 
https://replit.com/@AqsaAshfaq07/Number-Guessing-Game?v=1

from art import logo
from random import randint


def evaluate(number, guessed_num):
  if number < guessed_num:
    return "Too high!"
  elif number > guessed_num:
    return "Too low!"
  elif number == guessed_num:
    return "You got it. \nYou WIN!!"
  else:
    return "Enter a valid number!"


def main():
  print(logo)
  print(
    "Welcome to the Number Guessing Game!! \nI am thinking of a number between 1 and 100"
  )
  num = randint(0, 100)
  difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")

  if difficulty == "hard":
    attempts_left = 5
    while attempts_left <= 5:
      guess = int(
        input(
          f"You have {attempts_left} attempts left to guess a number. \nMake a guess:  "
        ))
      print(evaluate(num, guess))
      attempts_left -= 1
      if num == guess:
        break
      else:
        continue

  elif difficulty == "easy":
    attempts = 10
    while attempts <= 10:
      guess = int(
        input(
          f"You have {attempts} attempts left to guess a number. \nMake a guess:  "
        ))
      print(evaluate(num, guess))
      attempts -= 1
      if num == guess:
        break
      else:
        continue
      attempts -= 1

  else:
    print("Enter a valid input!!")


main()