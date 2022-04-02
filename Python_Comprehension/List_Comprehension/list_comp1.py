# Find square of a number
num = [1, 2, 3, 4, 5]
squares = []

# Normal for loop
for n in num:
    squares.append(n**2)

print("Normal for loop: ", squares)

# List comprehension
squares = [n**2 for n in num]

print("List comprehension: ", squares)


