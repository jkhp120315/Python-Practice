"""
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.

Function Description
Complete the print_full_name function in the editor below.

print_full_name has the following parameters:

string first: the first name
string last: the last name
Prints

string: 'Hello  ! You just delved into python' where  and  are replaced with  and .
"""

def print_full_name(first,last):
    str = "Hello firstname lastname! You just delved into python."
    newstr = str.replace("firstname",first).replace("lastname",last)
    print(newstr)
    
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print_full_name(first_name, last_name)


