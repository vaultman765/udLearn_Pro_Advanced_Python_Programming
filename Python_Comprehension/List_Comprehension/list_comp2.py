# Find common numbers between lists
list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5, 6]

intersection = []

# Normal for loop
for x in list1:
    for y in list2:
        if x == y:
            intersection.append(x)

print("list1 and list2 intersection using for loop: ", intersection)

# List comprehension
intersection = [x for x in list1 for y in list2 if x == y]

print("list1 and list2 intersection using list comprehension: ", intersection)

# Return numbers not equal as a tuple (cartesian product of non-common)
non_common_elements = [(x, y) for x in list1 for y in list2 if x != y]

print("Non-common elements: ", non_common_elements)


