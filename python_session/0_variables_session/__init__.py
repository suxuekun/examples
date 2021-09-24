x = 1
y = 2
z = x+y
print(z)

print("----")

a = "a"
b = "b"
c = a+b

print(c)
print("----")

p = str(a)+str(x)
print(p)
print("----")


d = 1
d = "string"
d = True
print(d)
print("----")


a = 3
x = str(a)
y = int(a)
z = float(a)
p = bool(a)
print(x,y,z,p)
print("----")

l = [0,"",False,0.0,[],{},None]

for item in l:
    if item:
        print("if",item ,'is True')
    else:
        print("if",item, 'is False')

print("----")

x = "global x"

def func():
    x = 'local x'
    print(x)
func()
print(x)
func()





