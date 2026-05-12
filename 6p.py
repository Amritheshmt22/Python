# Logical operators
# NOT
a = 50
b = 30
print (not True) # False
print (not (a>b)) # False

# AND
val1 = True
val2 = True
print (True and True) # True
print (True and False) # False
print("and operator:", val1 and val2)
print("and operator:", (a==b) and (a>b))

# OR
val1 = True
val2 = False
print("OR operator:", val1 or val2)
print("OR operator:", (a==b) or (a>b))
