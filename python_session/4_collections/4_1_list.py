#list
l1=[1,2,3,4,5,6,7,8,9]

# slice list[start:end(not included):step]
res = [
    l1[1:3],#[2,3]
    l1[-1],#9
    l1[:3],#[1,2,3]
    l1[5:],#[6,7,8,9]
    l1[::2],#[1,3,5,7,9]
    l1[::-1],
]
print(res)

# functions
l2 = [1,2,3]
l3 = ['a','b','c']
l2.append(4)
print(l2)
l2.insert(2,'inserted item')
print(l2)
l2.extend(l3)
print(l2)
l2.pop(2)
print(l2)
del l2[5]
print(l2)
l2.clear()
print(l2)



#loop

l3 = range(1,10)
print(list(l3))
for x in l3:
    print(x)

l4 = [x for x in l3 if x%2==1]
print(l4)

l5 = [
      [1,3,5,7,9],
      [2,4,6,8,10],
      ['a','b','c','d','e'],
     ]

flat_list = [item for sublist in l5 for item in sublist]
print(flat_list)

flat_list2=[]
for sublist in l5:
    for item in sublist:
        flat_list2.append(item)
print(flat_list2)

#sort
l0 = [101,94,72,83,28,37,59,15]
l6 = l0[:]
l7=l6.copy()
l8=l6.copy()
l9=l6.copy()

l6.sort()
l7.sort(reverse=True)
l8.sort(key = lambda x:x%10)

def list_compare_value_func(n):
    return abs(n-50)

l9.sort(key = list_compare_value_func)

print(l6)
print(l7)
print(l8)
print(l9)
print("----")
print(l0)
print([list_compare_value_func(x) for x in l0])
print("----")

#join
fruits =["apple",'banana','orange']
res = "i like "+",".join(fruits)
print(res)


