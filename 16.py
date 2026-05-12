##SETS
## set is used for store the values in key and value pair
## sets is the collection of the unordered items
## Each element in a set must be unique and immutable
## sets are mutable(can change)
## sets are unordered(not in order)
## sets are written in curly braces{}
## we can store any type of things like tuple,list,anything no issue complete acceptable.
## we can't use duplicate key.
## also in the set we can't store key value pair just we can store values.
## also if we store 2 values in a set it wont show the duplicate neither error only it willignore and keep.typ
##_______________________________________________________________________##
# empty_set = set() #this is the only way to create empty set
# print(type(empty_set))
##_______________________________________________________________________##
set = {1,2,3,4,5,6,7,8,9,10}
print(set)
##_______________________________________________________________________##
set.add(12) #This is used for add the values
print(set)
##_______________________________________________________________________##
set.remove(2) #If we remove the value which is not in the set it will show the error
print(set)
##_______________________________________________________________________## 
set.clear() #This is used for remove all the values
print(set)
##_______________________________________________________________________##
set.add((1,2,3)) #we can add tuple in set
print(set)
##_______________________________________________________________________##
# set.add([1,2,3]) #we can't add list in set    
# print(set)
##_______________________________________________________________________##
set.update([11,21,31]) #we can add list in set
print(set)
##_______________________________________________________________________##
print(len(set))
##_______________________________________________________________________##
print(set.pop())#this is used for remove the values
print(set.pop())#this is used for remove the values
##_______________________________________________________________________##

s1={1,2,3}
s2={3,4,5}
print(s1.union(s2)) #union means all the values
print(s1.intersection(s2)) #intersection means common values
print(s1.difference(s2)) #difference means not common values
print(s1.symmetric_difference(s2)) #symmetric difference means not common values