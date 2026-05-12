##---DICTIONARY---#
## dict is used for store the values in key and value pair
## dict is mutable(can change)
## dict is unordered(not in order)
## dict is written in curly braces{}
## we can store any type of things like tuple,list,anything no issue complete acceptable.
## we can't use duplicate key.

info = {
    "name": "a",
    "learning": "python",
    "marks": 99,
    "is_adult": True,
    12:21
}
null_dict = {}
print(null_dict)
print(info)
print(type(info))
print(info["name"])
info["name"] = "befg" #overwrite
info['surname'] = "23"
print(info)
#nested dictionary
student = {
    "name" : "rahul",
    "sub": {
        "Phy":97,
        "chem":87
    }
}
print(student)
print(student["sub"]["chem"]) #using for printing seperately from nested 
#_______________________________________________________________________##
print(student.keys()) #to get keys inthis dictionary
#_______________________________________________________________________##
print(list(student.keys()))
#_______________________________________________________________________##
print(len(student)) #to find the length of list
#_______________________________________________________________________##
print(list(student.values())) #to getting the values
#_______________________________________________________________________##
print(list(student.items())) #here we can get all pair wise we will get
#_______________________________________________________________________##
pairs = list(student.items())#THIS IS USING FOR GET SEPERATE PAIRS
print(pairs[0])              #THIS IS USING FOR GET SEPERATE PAIRS
#_______________________________________________________________________##
print(student.get("name")) #in here values through the key
print(student["name"]) # without using get also we will get ame result, but if this line got error the remaining will also get the error ,
                       # so thats why we using ".get" it will return only "None"rest everything will get execute
#_______________________________________________________________________##
student.update({"age" : "21"})
print(student)
#above and below will work as same no issue both are same
new = {"age" : 21}
student.update(new)
print(student)
#also if we want updaye old data into new it will also work
new = {"name" : "Amrithesh"}
student.update(new)
print(student)
##_______________________________________________________________________##