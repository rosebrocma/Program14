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
#Testing len on objects of type CustomSet
print("Testing len on set1", end= " ");print(len(set1))
print("Testing len on set2", end= " ");print(len(set2))
#Testing >= or superset
print("Creating and printing set3", end=" ");set3 = CustomSet([1,3,1])
print(set3)
print("Creating and printing set4", end=" ");set4 = CustomSet([1,2,3,4,4])
print(set4)
print("testing whether set3 is a superset of set4",end=" ") 
result = (set3 >= set4)
print(result)
print("Testing whether set4 is a superset of set3",end = " ")
if set4 >= set3: print("Yes")
else:
    print("not a subset")


