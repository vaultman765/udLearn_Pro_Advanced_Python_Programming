input1 = [1, 2, 3, 4, 4, 5, 6, 7, 7, 7]
output1 = (var for var in input1 if var % 2 == 0)

print("Output values using Generator Comprehension: ", end='')
for var in output1:
    print(var, end='')
