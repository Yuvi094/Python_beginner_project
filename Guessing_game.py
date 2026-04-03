import random

print("------------------------------------------------------")
print("        GUESS THE NUMBER        ")
print("------------------------------------------------------")

user_name = input("Enter your name: ")

# We take the difficulty input outside the function
print("\n1: Easy (1-50) | 2: Medium (1-100) | 3: Hard (1-500)")
print("4: Extreme (1-1000) | 5: Impossible (1-10000)")

try:
    difficulty_choice = int(input("Select difficulty: "))
except ValueError:
    difficulty_choice = 2 

def guessing_game(diff):
    # Determine the random number based on difficulty
    match diff:
        case 1:  
            rand_num = random.randint(1, 50)
        case 2:
            rand_num = random.randint(1, 100)
        case 3:
            rand_num = random.randint(1, 500)
        case 4: 
            rand_num = random.randint(1, 1000)
        case 5: 
            rand_num = random.randint(1, 10000)
        case _:
            print("Invalid input, setting range to 1-100.")
            rand_num = random.randint(1, 100)

    attempts = 0
    
    while True:
        try:
            num = int(input("\nPick a number: "))
            attempts += 1
            
            if num == rand_num:
                print(f"You have the lucky number! It took you {attempts} attempts.")
                
                return attempts 
            
            print("WRONG")
            hint = input("Want a hint? (y/n): ").lower()
            
            if hint == "y":
                if num > rand_num:
                    print("Hint: Go lower")
                else:
                    print("Hint: Go higher")
                    
        except ValueError:
            print("Invalid input. Please enter a number.")

def result_name(name, final_score):
    print("-------------------------------")
    if final_score <= 5:
        print(f"Great game, {name}!")
    elif final_score <= 10:
        print(f"Good try, {name}!")
    else:
        print(f"Can improve, {name}!")
score = guessing_game(difficulty_choice)
result_name(user_name, score)

print("\nThank you for playing! Congrats if you got it!")
