### To covert input string in upper case
str1 = 'GeeksforGeeks'
upper = lambda string: string.upper()
print(upper(str1))
print("")


### Condition Checking Using Python lambda function
a = lambda b: b if b > 5 else 7
print(a(1))


### sqare function using lambda function
a = lambda b: b**2
print(a(9))

###Python Lambda Function with List Comprehension
is_evenlist = [lambda arg=x: arg * 10 for x in range(1,5)]
for item in is_evenlist:
    print(item())


### Find Max number
findMax = lambda x,y: x if x>y else y
print(f"Max Number is {findMax(95,45)}")