# slice string
s = "hello world"
print(s[2:5])
print(s[0:10:2])

# string formats

s2 = "hello {}"
res = s2.format('john')
print(res)

s3 = "my name is {} , I am {} years old"
res = s3.format("john",5)
print(res)


s4 = "my son's name is {0}, {0} is {1} years old"
res = s4.format("john",5)
print(res)

s5 = "my son's name is {name}, {name} is {age} years old"
res = s5.format(name="john",age=10)
print(res)

#python3.6 f-string

name = "john"
age = 15
s6 = f"my son's name is {name}, {name} is {age} years old"
print(s6)

# expression in f-string
s7 = f'1+2 = {1+2}'
print(s7)

def func(a,b,c):
    return 2*a+3*b+c

a = 10
b = 5
c = 7
s8 = f'a={a},b={b},c={c},then 2a+3b+c={func(a,b,c)}'
print(s8)


#string functions
#https://www.w3schools.com/python/python_strings_methods.asp
s9="123456"
print(s9,'is numeric',s9.isnumeric())



