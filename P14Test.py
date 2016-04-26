from modCustomSet import *
#testing str method for both set1 and set2
print("Creating and printing set1", end= " ");set1 =CustomSet([1,1,2,2,3,3])
print(set1)
print("Creating and printing set2", end= " ");set2 = CustomSet([1,2,3,4,4])
print(set2)
#Testing <= or subset
print("Testing subset if set1 is a subset of set2", end= " ")
subset =(set1 <= set2)
print(subset)
print("Testing if set2 is a subset of set1", end= " ")
if set2 <= set1:print("Yes")
else:
    print("not a subset")


