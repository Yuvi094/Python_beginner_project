

import random
print("--------------------------------")
print("       GUESS THE NUMBER     ")
print("--------------------------------")

Diff = int(input("Press 1 for easy difficulty(1-50)\n"
      "Press 2 for medium difficulty(1-100)\n"
      "Press 3 for hard difficulty(1-500)\n"
      "press 4 for extreme difficulty(1-1000)\n"
      "press 5 for impossible difficulty(1-10000)"
       ))
print("--------------------------------")
roasts = [
    "Nah bro... even ChatGPT guesses better blindfolded.",
    "WRONG! Are you typing with oven mitts on?",
    "That's so off it's basically performance art.",
    "Error 404: Correct guess not found. Skill issue detected.",
    "Bro the number just filed a restraining order against your guesses.",
    "You're not getting warmer... you're literally freezing.",
    "That's not even in the same postcode as the answer 😂",
    "Keep going king, the disappointment is building nicely.",
    "At this rate the number will retire before you find it.",
    "Bold of you to assume you know what you're doing.",
    "My WiFi has more connection than you do right now.",
    "You're guessing like it's interpretive dance.",
    "Patna traffic makes better decisions than your last guess.",
    "The number is embarrassed for you right now."
]
def guessing_game():  
  attempts = 0
  match Diff:
    case 1:
     rand_num = random.randint(1,50)
    case 2:
      rand_num = random.randint(1,100)
    case 3:
      rand_num = random.randint(1,500)
    case 4:
      rand_num = random.randint(1,500)
    case 5:
      rand_num = random.randint(1,500)
    case _:
      print("Inavlid Input. TRY AGAIN")
  while True:
     try:
      num = int(input("Pick any number  : "))  
      attempts += 1
      
      if num == rand_num :
          print("You have the lucky number")
          print(f"You took {attempts} attempts") 
          break 
      print("WRONG")
      if num  >rand_num :
          print("GO lower")
      elif num < rand_num: 
          print("GO higher")
          print(random.choice(roasts))
     except ValueError:
       print("Try agin.. Invalid input")
       print("-------------------------------")

guessing_game()
print("Thank you for playing this Number guessing game")
print("-------------------------------")

print("Congrats if you got the lucky number")
print("-------------------------------")
