"""6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each piece
of information stored in your dictionary."""

print("=======INFORMATION======")
print("==========6-1==========")
information = {
    "first_name": "kripesh",
    "last_name": "subedi",
    "age": 19,
    "city": "Nepalgunj",
}
print(information["first_name"])
print(information["last_name"])
print(information["age"])
print(information["city"])

"""6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
Think of five names, and use them as keys in your dictionary. Think of a favorite 
umber for each person, and store each as a value in your dictionary. Print 
each person’s name and their favorite number. For even more fun, poll a few 
friends and get some actual data for your program."""
print("=====FAVORITE_NUMBER======")
print("=====6-2======")
favorite_number = {
    "kashish": 3,
    "kripesh": 7,
    "roshan": 10,
    "deepson": 8,
    "haaland": 9,
}
#for number in favorite_number:
#    print(number, favorite_number[number])
for name, number in favorite_number.items():
    print(f"{name.title()}'s favorite number is {number}.")