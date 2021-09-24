x = 5
print(type(x))

print(type)
print(type(type(type)))

y = 1j
print(y)
print(complex(x))
z = x+y
print(z,type(z))

l=[
    '1',
    1,
    1.0,
    1j,
    [1],
    {'1':1},
    range(1),
    {1},
    frozenset({1}),
    True,
    b'1',
    bytearray(),
    memoryview(bytes(5))
]

[print(i,type(i)) for i in l]



#mutable & immutable
x=10
y=x
print(x,y)
y=12
print(x,y)

x = [1,2,3]
y = x
print(x,y)
y.append(4)
print(x,y)

#mutable:list,dict,set  ,  immutable: number(float,int,complex,bool),string,tuples,frozenset

