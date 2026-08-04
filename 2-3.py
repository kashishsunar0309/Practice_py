#2-3 execise.
person = "Eric"
message = f"Hello {person}, would you like to learn some Python today?"
print(message)

#2-4 
name = "Eric"
message_1 = f"Hello {name}, would you like to learn some Python today?"
print(name.lower())
print(name.upper())
print(name.title())

#2-5
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

#2-6
famous_person = "Albert Einstein"
message = f'{famous_person} once said, “A person who never made a mistake never tried anything new.”'
print(message)

# 2-7 Stripping Names
person_name = "\t\n  Deepson  \n\t"

print("Original with whitespace:")
print(person_name)

print("\nUsing rstrip():")
print(person_name.rstrip())

print("\nUsing lstrip():")
print(person_name.lstrip())

print("\nUsing strip():")
print(person_name.strip())

#2-8

filename = 'python_notes.txt'
print(filename.removesuffix(".txt"))