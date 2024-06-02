import functools

listNumbers = [1,2,3,34,5,7]

# Find sum of all the numbers of the list
answer = functools.reduce(lambda x,y:x+y,listNumbers)
print(answer)

# Find Max Number from the list
answer = functools.reduce(lambda x,y:x if x>y else y, listNumbers )
print(answer)