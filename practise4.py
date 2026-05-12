#WAP to swap the value of two variables a and b without using a third temporary variable

a = int(input("N1: "))
b = int(input("N1: "))

print(f"Before Swapping: {a}, {b}")
a, b = b, a
print(f"after swapping: {a}, {b}")
