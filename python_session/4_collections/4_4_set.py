s = {1,2,3,4,5}

for x in s:
    print(x)

s.add(6)
print(s)
s.add(1)
print(s)
s.update({1,3,5,7,9})
print(s)
s.remove(6)
print(s)

set1 = {"a", "b" , "c",4}
set2 = {1, 2, 3,4}

set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)

#other functions
#https://www.w3schools.com/python/python_sets_methods.asp


#remove same element from list
l=[1,1,2,2,3,3,4,5,6,7,8,9]
l2 = list(set(l))
print(l2)
