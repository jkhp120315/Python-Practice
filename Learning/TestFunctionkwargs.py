"""
**kwargs argment can take any number keyword arguments in form of key / pair value
"""
def displayinfo(**kwargs):
    sum = 0
    for k,v in kwargs.items():
        print(k,"->",v)

displayinfo(a='himanshu',b='Satya',c='Rob')