def findSqrt(list):
    print(f"List of numbers - {list}") 
    answer = map(lambda x:x**2,list)
    return answer

def findOddEven(list):
    print(f"List of numbers - {list}") 
    answer = map(lambda x: 'odd' if x%2 != 0 else 'even',list)
    return answer

listNumber = [1,2,3,4,19]

# Find sqrt of list numbers
sqrtofNumbers = findSqrt(listNumber)   
print(f"Square root of numbers - {list(sqrtofNumbers)}")

# printing odd even numbers
print(f"Odd Even Numbers list {list(findOddEven(listNumber))}")