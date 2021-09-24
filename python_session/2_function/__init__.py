def func():
    print('hello world')

func()

def func1(x):
    print('hello',x)

func1('john')

def func2(x='john'):
    print('hello',x)

func2()

def func3(x=[]):
    x.append('1')
    print(x)
    return x

func3()
func3()
func3()

def func3_1(x={}):
    if (x.get('x')):
        x['x'] +=1
    else:
        x['x'] = 1
    print(x)
    return x

x = func3_1()
y = func3_1()
z = func3_1()



print(x,y,z)

def func4(a,b,c=None,*args,**kwargs):
    print(a,b,c,args,kwargs)

func4(1,2,3,4,5,6,d=10,e=20)

args =(1,2,3,4,5,6)
kwargs = {'d':10,'e':20}
func4(*args,**kwargs)

# args always before kwargs
# bad example : func4(a=10,2,3)

f = lambda a : a + 10
print(f(10))
print(lambda a:a +10)


#build in functions
#https://www.w3schools.com/python/python_ref_functions.asp