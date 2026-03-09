

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
      rand_num = random.randint(1,1000)
    case 5:
      rand_num = random.randint(1,10000)
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
      hint = str(input("Want a hint? (y/n)"))
      if hint.lower() == "y":
        if num  >rand_num :
          print("GO lower")
        elif num < rand_num: 
          print("GO higher")
      elif hint.lower() == "n":
        print("You will get no hints")
      else:
        print("Invalid Input")
     except ValueError:
       print("Try agin.. Invalid input")
       print("-------------------------------")

guessing_game()
print("Thank you for playing this Number guessing game")
print("-------------------------------")

print("Congrats if you got the lucky number")
print("-------------------------------")
