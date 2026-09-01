# 4-3 Counting to Twenty
for value in range(1, 21):
    print(value)

# 4-4 One Million
numbers = list(range(1, 1000001))
# print(numbers)  

# 4-5 Summing a Million
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))

# 4-6 Odd Numbers
for x in range(1, 21, 2):
    print(x)

# 4-7 Threes
for y in range(3, 31, 3):
    print(y)

# 4-8 Cubes
cubes = []
for k in range(1, 11):
    cubes.append(k ** 3)
print(cubes)

# 4-9 Cube Comprehension
cubes = [z ** 3 for z in range(1, 11)]
print(cubes)