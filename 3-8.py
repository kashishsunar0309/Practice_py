# 3-8 
places = ["Tokyo", "New York", "Washington", "Hong Kong", "Los Angeles", "London", "New Delhi"]

print("Original list:")
print(places)

print("\nAlphabetical order (using sorted()):")
print(sorted(places))

print("\nOriginal list still the same:")
print(places)

print("\nReverse-alphabetical order (using sorted()):")
print(sorted(places, reverse=True))

print("\nOriginal list still the same:")
print(places)

print("\nUsing reverse():")
places.reverse()
print(places)

print("\nUsing reverse() again (back to original):")
places.reverse()
print(places)

print("\nUsing sort() - alphabetical:")
places.sort()
print(places)

print("\nUsing sort(reverse=True) - reverse alphabetical:")
places.sort(reverse=True)
print(places)

# 3-9
guests = ["Roshan", "Kripesh", "Deepson"]
print("\nNumber of people invited to dinner:", len(guests))

#3-10
country = ["America", "Australia", "Germany", "Japan", "India", "Cape Verde"]

print("--- Original ---")
print(country)

print("\n--- append() ---")
country.append("Norway")
print(country)

print("\n--- insert() ---")
country.insert(0, "Brazil")
print(country)

print("\n--- pop() ---")
removed = country.pop(0)
print("Removed:", removed)
print(country)

print("\n--- remove() ---")
country.remove("India")
print(country)

print("\n--- sorted() (temporary) ---")
print(sorted(country))
print("Original still same:", country)

print("\n--- reverse() ---")
country.reverse()
print(country)

print("\n--- sort() ---")
country.sort()
print(country)

print("\n--- sort(reverse=True) ---")
country.sort(reverse=True)
print(country)

print("\n--- del ---")
del country[2]
print(country)

print("\n--- len() ---")
print("Total countries left:", len(country))