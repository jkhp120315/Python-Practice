listofNumber = [1,2,3,4,5,6]

#Display list containing numbers > 3 in above list

answer = filter(lambda x: x>3 ,listofNumber) 
print(list(answer))



fruits = ['apple' , 'avacaode' , 'mango' , 'banana']
# Display list of fruits start with letter "a"

answer = filter(lambda x:x.startswith('a'),fruits)
print(list(answer))

h = [1,2,3,4,5,6,3]
answer = filter(lambda x: h[x]==3,h)
print(list(answer))