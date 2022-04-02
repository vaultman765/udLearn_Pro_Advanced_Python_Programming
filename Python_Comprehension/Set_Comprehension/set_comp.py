input1 = [1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 7, 7, 7, 8]

# Using for loop
output1 = set()
for var in input1:
    if var % 2 == 0:
        output1.add(var)

print(output1)

# Using set comprehension
output1 = {var for var in input1 if var % 2 == 0}
print(output1)
