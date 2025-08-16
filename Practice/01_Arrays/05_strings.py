"""In Python, strings are a fundamental data type these are arrays of bytes representing unicode charecters and can be used in various data structures to manipulate and store text. Here are some ways strings can be used in different Python data structures:

trings support various operations that make them versatile for text manipulation.

Concatenation: s1 + s2
Repetition: s * 3
Slicing: s[1:4]
Methods: s.upper(), s.lower(), s.split(), s.strip(), etc.
"""

str1 = "Udacity"
 
print(len(str1))

print(str1.lower())
print(str1.upper())

#slicing 
print(str1[1:6])
print(str1[:6])
print(str1[1:])

#negative indexing 
print(str1[-1])
print(str1[-6:-1])

