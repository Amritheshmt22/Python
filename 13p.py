## marks1 = 98
## marks2 = 95
## marks3 = 97
## marks4 = 99
## marks5 = 93
## like this we used to store the values but now we can use __LIST__by simply in one line.

# #---LIST---#
# marks = [96, 95, 98, 97, 99]
# print(marks)
# print(type(marks))
# print(marks[1])

# student = ["abc",123, "Delhi"]
# print(student)
# student[0] = "def"
# print(student)

# marks = [96, 95, 98, 97, 99]
# print(marks[-3:-1])
marks = [96, 95, 98, 97, 99]
marks.append(4)         #it will add at last
marks.sort()            #Ascending order    
marks.sort(reverse=True)#Descending order
marks.insert(3,90)
marks.remove(95)
marks.pop(5)
print(marks)