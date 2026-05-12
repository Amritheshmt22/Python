#wap to ask the user to enter names of their 3 favorite movies & store them in list
mov = []
mov.append(input("enter 1st: "))
mov.append(input("enter 2nd: "))
mov.append(input("enter 3rd: "))

print(mov)

# so this is the one way(ABOVE)
# Next one is (BELOW)
mov = []
m1 = input("1: ")
mov.append(m1)
m1 = input("2: ")
mov.append(m1)
m1 = input("3: ")
mov.append(m1)

print(mov)