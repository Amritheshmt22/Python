# Type conversion
# in conversion python do the type conversion automatically but in casting we have to do it manually.
# eg\
a = 2
b = 3.5
print(a+b) # 5.5

# in here it will convert a into float and then do the addition but if we want to do it manually then we can do it by using casting
c = float(a)
print(c) # 2.0
print(type(c)) # <class 'float'>

# but when string came *int* will not convert it into *int* or float it will just concatenate it

a = 3.14
a = str(a)

print(a) # 3.14
print(type(a)) # <class 'str'>