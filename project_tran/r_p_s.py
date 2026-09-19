import random
print("Rock-Paper-Scissor")
score = 0
for i in range(1,10):
    choice = input("Enter your choice: ")
    comp_choice = random.choice(['rock','paper','scissors'])
    if (choice == comp_choice):
        print("DRAW-NEXT-TIME-THAT-MINE")
    elif(comp_choice == 'rock') and (choice == 'scissors'):
        print("YOU LOST...")
        score -=1
    elif(comp_choice == 'paper') and (choice == 'rock'):
        print("YOU LOST...")
        score -=1
    elif(comp_choice == 'scissors') and (choice == 'paper'):
        print("YOU LOST...")
    else:
        print("YOU WON")
        score +=1
print(f"The final score is {score}")