#   PICK A NUMBER!
#  This time YOU pick a number and the program has to 
# guess what number you're thinking by making you questions.
#  You have to indicate if the number is higher by answering "mayor", or
# if it's lower by answering "minor", or if it is correct by answering "correct".
#  Be careful, if you answer anything else it will know, and if maaybe if you're
# not playing by the rules it might expose you. :)

# Before playin/reading, try to do it yourself.



print("--- PICK A NUMBER! ---")
print("Pick a number from 1 to 100.")
from random import randint

min = 1
max = 100

for attempts in range(10):
  
  try:
    secret_number = randint(min, max)
    
    print(f"Is your number {secret_number}?")
    answer = input("Enter 'mayor', 'minor', or 'correct':").lower()

    if answer == "correct" :
      print(f"GREAT! I've guest the {secret_number} in {attempts} attempts!\nLet's play again!")
      break

    elif answer == "mayor" :
      min = secret_number + 1

    elif answer == "minor" :
      max = secret_number - 1
    
    else :
      print("Please only enter 'mayor', 'minor', or 'correct':")

  except ValueError :
    print("That's weird... I think someone is cheating...")
    break
  except Exception as e:
    print(f"¡Error! - {e}")
  
  finally:
    print()
    attempts += 1