dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

new_dict = {k: v for (k, v) in dict1.items() if v > 3}
print(new_dict)

new_dict = {k: v for (k, v) in dict1.items() if v > 3 if v % 2 == 0}
print(new_dict)

new_dict = {k: ('even number' if v % 2 == 0 else 'odd number') for (k, v) in dict1.items()}
print(new_dict)
