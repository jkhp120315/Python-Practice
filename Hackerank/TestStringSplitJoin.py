
def split_and_join(str):
    a = str.split()
    b = "-".join(a)
    return b
    
str = input("Enter String: ")
result = split_and_join(str)
print(result)