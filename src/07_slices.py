"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print("Output second element:")
print(a[1])
print('\n')

# Output the second-to-last element: 9
print("Output second-to-last element:")
print(a[-1])
print('\n')

# Output the last three elements in the array: [7, 9, 6]
print("Output last 3 elements:")
print(a[-3:])
print('\n')

# Output the two middle elements in the array: [1, 7]
print("Output 2 middle elements:")
aLen = len(a)

# if length of a is odd, there is only one middle element
if aLen % 2 == 1:
    print('hi')
    print(a[aLen // 2])
# if length of a is even, there are 2 middle elements
elif aLen % 2 == 0: 
    firstIndex = (aLen // 2) - 1
    lastIndex = (aLen // 2) + 1

    print(a[firstIndex:lastIndex])

print('\n')

# Output every element except the first one: [4, 1, 7, 9, 6]
print("Output every element except the first one:")
print(a[1:])
print('\n')

# Output every element except the last one: [2, 4, 1, 7, 9]
print("Output every element except the last one:")
print(a[:-1])
print('\n')

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print("Output the 8th-12th characters:")
print(s[7:12])