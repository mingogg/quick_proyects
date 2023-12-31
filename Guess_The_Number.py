# This is a fun game to create, to learn some functions and logic.
# Although it's easy to create, you can still apply some good practice coding and
# make a legible code for everyone. That is the point of this.

# The main thing it's to develop an interactive game called "Guess the Secret Number".
# RULES:
# - The program has to select a random number between a specific range (in my case 1-100).
# - The player has a limited amount of attempts to guess the secret number (in my case 10).
# TRY IT YOURSELF BEFORE READING THE CODE!

print("--- GUESS THE SECRET NUMBER! ---")
print("A number between 1 and 100 has been selected.")
print("Guess wich one!\n")

from random import randint

attempts = 1
random_num = randint(1, 100)


while attempts < 11 :
  
  try:
    print(f"Attempt {attempts}/10.")
    user_num = int(input("What's guessing?"))
    
    if attempts == 10: 
      print(f"UPS! The secret number was: [{random_num}].\nGuess Again!")
    
    elif user_num < random_num :
      print(f"The secret number it's higher than {user_num}.")
    
    elif user_num > random_num :
      print(f"The secret number it's lower than {user_num}.")

    else:
      print(f"KACHING! You got it right! [{random_num}]\nAnd in [{attempts}] attempts, nice!")
      break
  
  except ValueError:
    print("Error! It has to be a integer.")
  except Exception as e:
    print(f"Error! {e}")
  
  finally:
    print()
    attempts += 1
