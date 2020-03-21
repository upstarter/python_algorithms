from pprint import pprint

# Useful Python String Methods:

# len() – Returns the length of the string
# s1 in s2 – Is s1 a substring of s2
# index(s1) – Returns the index of s1 in the string
# list(s1) – Converts s1 into a character array
# s1[i:j] – Get  the substring of s1 from i to j

x = "Cake"
y = "Cookie"

x + " & " + y
# Repeat
x * 2

# Range Slicing
z1 = x[2:]

print(z1)

# Slicing
z2 = y[0] + y[1]

print(z2)

str1 = "Cake 4 U"
str2 = "404"
len(str1)  # off by one for iter!
str1.isdigit()
# False
str2.isdigit()
# True
str1.replace("4 U", str2)
# => 'Cake 404'

# substrings
str1 = "I got you a cookie"
str2 = "cook"
str1.find(str2)
