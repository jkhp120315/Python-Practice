"""
*args argment can take any number arguments in form of tuple
"""
def addnumbers(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

answer = addnumbers(4,5,6,10)
print(answer)