# All builtins methods
# 1. all()
""" all() return True if it id iterable else it will return False 
    if Iterable is empty it return True 
"""
print("hello")
li = [1,2,3,4]
print("to check list is iterable or not ::", all(li))

st = {1,2,3,4}
print("to check set is iterable or not::",all(st));

dt = {"a":1, "b":2, "c":3}
print("to check dict is iterable or not ::",all(dt))

tp = (1,2,3)
print("to check tuple is iterable or not ::",all(tp))
    
# if iterable is empty it return True

l,s,d,t=[],{},{},()
print(all(l),all(s),all(d),all(t))
