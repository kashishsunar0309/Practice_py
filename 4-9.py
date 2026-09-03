food = ['pizza', 'falafel', 'carrot cake', 'cannoli',"burger","chicken-chilly"]
print("The First Three Item :")
print(food[0:3])
print("The Middle Three Item: ")
print(food[2:5])
print("The Last Three Item: ")
print(food[-3:])
#4-10
my_pizzas = ["New York Style", "Neapolitan", "Deep Dish"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("cheese-pizza")
friend_pizzas.append("Marinara")
print("My favorite pizzas are:")
for x in my_pizzas:
  print(x)
print("My Friend Favorite pizzas are:")
for y in friend_pizzas:
  print(y)
print("===4-12===")
food_1 = ['cannoli',"burger","chicken-chilly"]
print("My Favorite Food:")
for z in food_1:
  print(z)
print("My Friend Favorite Food:")
food_2 =['pizza', 'falafel', 'carrot cake']
for a in food_2:
  print(a)