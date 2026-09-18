questions = ['which country made dark?',
             'which country made prison-break?',
             'which coutnry made money-heist?',
             'which country made peaky blinder?',
             'who is the rich character in the dark knight?']
answer = ['germany','america','spain','england','bruce wine']
sum = 0
for i in  range(len(questions)):
  print(questions[i])
  print("="*30)
  guess = input("Enter the answer: ")
  print(30*"=")
  print()
  if guess.lower() == answer[i].lower():
    print("-YOU-GOT-10-MARKS-")
    sum += 10
  else:
    print("Wrong answer")

print(f"The final result is {sum}.")