#---TUPLES---#
# list is using for mutable(can change) but tuple is using for immutable(can't change, like string)
# here we use parenthesis()

tup = (1, 2, 13, 4, 13)
print(type(tup))
print(tup[2])
# tup[0] = 5 #its can be work in tuple
# so in this tuple one more feature like if we want to print a single number inside parenthesis we want to use "," 
# eg: tup =(1,)
# if we dont need the parenthesis we can just type 1 onle 
# tup =(1)
print(tup[1:3])
tup.index(1)
tup.count(2)
print(tup.index(1))
print(tup.count(13))