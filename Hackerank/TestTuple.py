N = int(input())

testTuple = ()

a = list(input().split())
b= []
c= ()
for i in a:
    b.append(int(i))

c=tuple(b)
print(hash(c))