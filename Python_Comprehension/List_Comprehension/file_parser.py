op = open("python.txt", "r")

output = [i for i in op if "is" in i]

print(output)
