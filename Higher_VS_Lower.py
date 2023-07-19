# For complete code and related files
https://replit.com/@AqsaAshfaq07/Higher-Lower-Game?v=1


# Step - 1 -> Make necessary Imports
from art import logo, vs
from game_date import data
import random
from replit import clear


# Step - 2 -> Write code to get random players
def find_players():
  player = random.choice(data)
  return player


# Step - 3 -> Display default stuff
def main(playerA, playerB):
  print(
    f"Compare A: {playerA['name']}, a {playerA['description']}, from {playerA['country']}"
  )
  print(vs)
  print(
    f"Against B:  {playerB['name']}, a {playerB['description']}, from {playerB['country']}"
  )


# Step - 4 -> Making Decisions and the complete soul of the project
def game():
  print(logo)
  playerA = find_players()
  playerB = find_players()
  score = 0
  should_continue = True

  while should_continue:
    playerA = playerB
    playerB = find_players()

    while playerA == playerB:
      playerB = find_players()

    main(playerA, playerB)
    # ask user to make a guess
    guess = input("Who is higher? Type 'A' or 'B':  ")
    clear()
    print(logo)
    # check if user's guess is right
    if (guess == 'A' and playerA['follower_count'] > playerB['follower_count']
        ) or (guess == 'B'
              and playerB['follower_count'] > playerA['follower_count']):
      score += 1
      print(f"You're right. Current Score : {score}")

    else:
      should_continue = False
      clear()
      print(f"{logo} \nYou're wrong!. Final Score: {score}")


game()