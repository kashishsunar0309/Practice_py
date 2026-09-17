"""1. Number Guessing Game (Best Starting Project)

Computer randomly chooses a number between 1–20
Player keeps guessing
Tell if the guess is too high or too low
Count how many attempts the player took

Why good? Uses loops + if-elif-else + variables very well."""
import random
print(35*"=")
print("||__RANDOM_NUMBER_GUESSING_GAME__||")
print("||*************RULE**************||")
print("||_______YOU_HAVE_ONLY_CHANCE____||")
print("||||||||||-------10-------|||||||||")
print(35*"=")
secret_number = random.randint(1,20)
attempt = 0;
for i in range(1,10):
  number = int(input("Enter the number: "))
  attempt += 1
  
  if (number==secret_number):
      print(f"=====YOU===WON===THE===GAME==== in {attempt} attempts! Number was {secret_number}")
      break;
  elif number > secret_number:
    print(f"Lower number this :{number}")
  else:
    print(f"Higher then this number:{number}")
else:
  print(f"++++TRY__NEXT_BETTER_LUCK_SECRET__NUMBER___IS___{secret_number}++++")