# #1---Store the word meanings in a python dictionary:
# # dict={
# #     "table" :["a piece of furniture","list of facts and figure"],
# #     "cat":"a small animal"
    
# # }

# # print(dict)

# #2---you are given a list of subjects for students . Assume one class 

#sub={
#    "python", "java", "c", "c++", "java script", "python", "java", "c++", "java" ,"python", "java", "c"
#}
#
#print(len(sub))

##3--- wap to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionar and add one bye one 
##use subject as key and marks as values

# marks = {}
# x = int(input("Enter the marks of Physics: "))
# marks.update({"Physics": x})
# y = int(input("Enter the marks of Chemistry: "))
# marks.update({"Chemistry": y})
# z = int(input("Enter the marks of Maths: "))
# marks.update({"Maths": z})

# print(marks)

##4-- figure out way to store 9 & 9.0 as seperate values in the set.map
##(You can take help of built in data types)

val = {"9.0", 9}
print(val)
# we can see that we cant print the both same value like 9 and 9.0 its same .so if we ,-
#want to see in one set we have to use string value of 9.0 like "9.0".