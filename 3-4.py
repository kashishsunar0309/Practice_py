# 3-4 Guest List
print("==== 3-4 ====")
guests = ["Roshan", "Kripesh", "Deepson"]

print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")

print()
#3-5
print("====3-5=======")
print(f"Sorry, i can't invite you MR.{guests[1]}.")
guests[1] = "kashish"
print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")
print()
#3-6
print("====3-6=======")
print("Good news! I found a bigger dinner table.")
guests.insert(0,"ram")
guests.insert(3,"anish")
guests.append("ashish")
print(f"Dear {guests[0]}, I would like to invite you to dinner.")
print(f"Dear {guests[1]}, I would like to invite you to dinner.")
print(f"Dear {guests[2]}, I would like to invite you to dinner.")
print(f"Dear {guests[3]}, I would like to invite you to dinner.")
print(f"Dear {guests[4]}, I would like to invite you to dinner.")
print(f"Dear {guests[5]}, I would like to invite you to dinner.")
#3-7
print("==== 3-7 ====")
print("Sorry, the new table won't arrive in time. I can invite only two people.")

# Remove guests one by one until only 2 remain
removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Now only 2 guests left
print(f"Dear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")

# Empty the list
del guests[1]
del guests[0]

print("Final guest list:", guests)