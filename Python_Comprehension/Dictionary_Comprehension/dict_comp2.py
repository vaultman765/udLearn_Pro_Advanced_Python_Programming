# Normal for loop
dict1 = {}
for i in range(10):
    if i % 2 == 0:
        dict1[i] = i**2

print("Normal for loop squares: ", dict1)

# Dictionary comprehension
dict1 = {i: i ** 2 for i in range(10) if i % 2 == 0}
print("Dictionary comprehension for squares: ", dict1)
