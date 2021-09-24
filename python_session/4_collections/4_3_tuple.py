l = [1,2,3,4,5]
t = tuple(l)
print(t)

fruits = ('apple','banana','orange')

(red,yellow,orange) =fruits
print(red,yellow,orange)

def func():
    # your logic then return more than one values
    return 'apple','banana','orange'

fruits_tuple = func()
apple,banana,orange = func()
print(fruits_tuple)
print(apple,banana,orange)