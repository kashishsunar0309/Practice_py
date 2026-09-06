"""5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
describing each test and your prediction for the results of each test. Your code 
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line 
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another 
5 tests evaluate to False."""
vechile = "bus"
if (vechile == "bus"):
  print("You predit True. ")
else:
  print("You predit False.")
if (vechile == "car"):
  print("You predit True. ")
else:
  print("You predit False.")
#True Statement
age = 10
print(age>=5)
name = "kashish"
print(name == "kashish")
age = 18
age_0 = 25
print(age >= 18 and age_0 >= 18)
vechiles = ["car","plane","train"]
print("car" in vechiles)
print("motorcycle" not in vechiles)
#False Statement
print(age < 8)
print(age == 14 or age_0 <= 20)
print(name == "Ashish")
print("bicycle" in vechiles)
print("plane" not in vechiles)
"""5-2. More Conditional Tests: You don’t have to limit the number of tests you cre
ate to 10. If you want to try more comparisons, write more tests and add them 
to conditional_tests.py. Have at least one True and one False result for each of 
the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and less 
than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list"""
name = "Kripesh"
if name.lower() == "kripesh":
  print("Yes Equality")
else:
  print("NO Equality")
if name.lower() != "ram":
  print("NOT Equality")
else:
  print("Yes Equality")
num = 18
if num >= 18:
  print("Yes, you are adult now! ")
else:
  print("No you are kid! ")
if num <= 18:
  print("you can play hintdentseek. ")
else:
  print("No you cann't")
if num == 18:
  print("you predict True.")
else:
  print("You predict False. ")
if num != 20:
  print("True, Right ")
else:
  print("False, Wrong")
if (num >= 18 and num <=40):
  print("You are young ")
else:
  print("you are kid or old. ")
vechile_0 = ["car","plane","train"]
print("car" in vechile_0)
print("motorcycle" not in vechile_0)