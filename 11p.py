#Conditional statements

# If- Else
age1 = int(input("enter your age:"))
age=age1


if (age>=18):
    print("You are eligible")
    print("You can apply for licesence")
else:
    print("You aren't ")
    print("Better luck next time19")

# IF-elif-else
light = input("Enter the color of Light:")

if (light == "green"):
    print("you can Go")
elif(light == "red"):
    print("You want to Stop")
elif(light == "yellow"):
    print("You can go slowly")
else:
    print("Fuck OFF")

#grade students based on marks
mark = int(input("Enter your marks:"))

if (mark>=90):
    grade="A"
elif (90>mark and mark>=80):
    grade = "B"
elif (80>mark and mark>=70):
    grade = "C"
elif (70>mark and mark>=60):
    grade = "D"
else:
    grade = "E - Successfully Fucked"

print(f"this is your Mark: {grade}")

Nested if else Statement

age = int(input("enter your age:"))

if (age>=18):
    if (age<=80):
        result = "Can drive"
    else:
        result = "Can't"
else:
    result:"Cant" # type: ignore

print(f"Your result is:{result}")