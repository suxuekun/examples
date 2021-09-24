son={
    'name':'john',
    'age':10,
}
print(son,son.get('name'),son['age'],son.get('job','no job'))

l = range(5,10)#[5,6,7,8,9]
res = {str(item)+"th":str(item+10)+"s" for item in l}
print(res)

print(son.keys())
print(son.values())
print(son.items())

for key in son.keys():
    value = son[key]
    print(key,"==>",value)

for k,v in son.items():
    print(k,v)

son['job'] = "software developer"
print(son)
poped_value = son.pop('job')
print(son,poped_value)
son['friends']=['alice','bob']
print(son)

son_clone = son.copy()
son_clone['age']=11
print(son,son_clone)
son_clone['friends'].append('charles')
print(son,son_clone)# mutable immutable

# deepcopy
import copy
real_clone = copy.deepcopy(son)
real_clone['friends'].append('david')
print(son,real_clone)


super_man={
    'power':5,
    'pants':'s',
    'name':'super man'
}

son.update(super_man)
print(son)



son.clear()
print(son)

#other functions
#https://www.w3schools.com/python/python_dictionaries_methods.asp
