#WAP function that accepts 2 integers number if the product of 2 number is less than or equal to 1000 ,return their product and sum.

n1 = int(input("ENter the 1st number: "))
n2 = int(input("ENter the 2nd number: "))

if (n1 * n2 <=1000):
    print(f"the product is : {n1 * n2}")
else:
    print(f"the sum is : {n1 + n2}")

print(n1 * n2 if n1 * n2 <= 1000 else n1 + n2)





