    
"""
This program is about learning default arguments in function
"""

def findsum(a=1,b=5):
    return a + b

answer = findsum(7,6)
print(answer)
answer = findsum()
print(answer)