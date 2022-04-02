feh = {'temp1': 10, 'temp2': 20, 'temp3': 30, 'temp4': 40}

# Using lambda function
cel = list(map(lambda x: (float(5)/9) * (x - 32), feh.values()))
cel_dict = dict(zip(feh.keys(), cel))
print("Celsius values from lambda function: ", cel_dict)

# Using dictionary comprehension
cel_dict = {k: (float(5)/9) * (v - 32) for (k, v) in feh.items()}
print("Celsius values from dictionary comprehension: ", cel_dict)
