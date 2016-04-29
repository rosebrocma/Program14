from myMethods import *

c1 = CustomSet([1, 3, 5, 1])
c2 = CustomSet([1, 2, 3, 4])
c3 = CustomSet([])
c4 = CustomSet([])
print("Testing In", 1 in c1)
print("Testing In", 6 in c2)

c3 = c1 - c2

c4 = c2 - c1

print("Testing Difference:",c3)
print()
print("Testing Difference:",c4)

print()
c3 = c1  & c2
print("Testing Union", c3)
