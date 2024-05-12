"""
1 insert i e: Insert integer  at position .
2 print: Print the list.
3 remove e: Delete the first occurrence of integer .
4 append e: Insert integer  at the end of the list.
5 sort: Sort the list.
6 pop: Pop the last element from the list.
7 reverse: Reverse the list.
"""


N = int(input("Enter number of commmands you wish to run: "))
print(N)

commandList = ["insert","print","remove","append","sort","pop","reverse"]

resultList = []

for i in range(N):
    commandName = list(input("Enter Command - ").split())
    if(commandName[0] == "insert"):
        resultList.insert(int(commandName[1]),int(commandName[2]))
    elif(commandName[0] == "append"):
        resultList.append(int(commandName[1]))
    elif(commandName[0] == "remove"):
        if(int(commandName[1]) in resultList):
            resultList.remove(int(commandName[1])) 
    elif(commandName[0] == "sort"):
        resultList.sort()
    elif(commandName[0] == "pop"):
        resultList.pop()
    elif(commandName[0] == "reverse"):
        resultList.reverse()    
    else:
        print(resultList)