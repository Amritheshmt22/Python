# Input
name=input("Enter your name: ")
print("you entered",name)


val = input("Enter a number: ")
print(type(val),val)
# In this wheather we give or string or integer or float it will only show string.
# for that we want to do type conversion


int("5") # it will convert string into integer
val = int(input("Enter a number: "))
print(type(val),val)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = float(input("Enter your marks: "))

print("welcome",name)
print("your age is",age)
print("your marks are",marks)