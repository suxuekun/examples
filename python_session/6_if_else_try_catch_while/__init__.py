a = False
b = False

if a:
    pass
elif b:
    pass
else:
    pass


x = 10 if a else 20
print(x)

if a:
    x = 10
else:
    x = 20

y = 10 if a else 20 if b else 30

print(y)

x=10
y=20
z=30

if x<y<z:
    print('x<y<z')

if x<y and y<z:
    print('x<y and y<z')

if x<z>y:
    print('x<z>y')

# while condition: loop
i = 0
while True:
    print(i)
    i+=1
    if (i>10):break

i = 0
while (i<=10):# not (i>10)
    print(i)
    i+=1

x = 1
y = 1
try:
    a=x/y;
    a=list(None)
except ZeroDivisionError as e:
    print('error:', e)
except Exception as e:
    print('error:', e)
finally:
    print('no matter what happened , this block will be executed')



