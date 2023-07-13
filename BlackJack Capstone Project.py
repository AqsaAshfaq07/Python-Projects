from replit import clear
import random
from art import logo


def evaluate(dealer_sum, curr_sum):
  if dealer_sum > curr_sum:
    return "Dealer Win."
  elif dealer_sum < curr_sum:
    return "You Win!!"
  elif dealer_sum == 21 and len(dealer_card) == 2:
    return "You lose, the opponent has got a JACK!!."
  elif curr_sum == 21 and len(your_cards) == 2:
    return "You win, you've got a JACK!!."
  else:
    return "Draw"


should_continue = input(
  "Do you want to play this game? \nType 'yes' or 'no': \n")
if should_continue == 'yes':
  print(logo)

  # Assume the cards are drawn from here.
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  # Getting your cards
  first_num = random.choice(cards)
  second_num = random.choice(cards)
  your_cards = [first_num, second_num]

  # Getting Computer's cards
  dCard1 = random.choice(cards)
  dCard2 = random.choice(cards)
  dealer_card = [dCard1, dCard2]

  while sum(your_cards) <= 21 or sum(dealer_card) <= 21:

    print(f"Your cards: {your_cards} , current score: {sum(your_cards)}")
    print(f"Dealer has: {dealer_card[0]}")

    hit_stand = (input("Hit | Stand: \n")).lower()

    if hit_stand == "hit":
      third_num = random.choice(cards)
      your_cards.append(third_num)

      dCard3 = random.choice(cards)
      dealer_card.append(dCard3)

    elif hit_stand == "stand":
      break

    else:
      print("Please enter correct input!!")

  print(evaluate(sum(dealer_card), sum(your_cards)))
elif should_continue == "no":
  clear()

else:
  print("Please enter a valid value!!")