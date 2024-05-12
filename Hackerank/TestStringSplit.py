"""
Find a count of SubString in Main String

Input Main String - test abc hi kjkjk abc jiojio sds
SubString - abc

Output - 2
"""

def count_substring(string, sub_string):
        cnt = 0
        j=0
        for i in string:
            j=j+1
            print(j)
            if(sub_string in string): 
                cnt = cnt + 1
                a = string.index(sub_string)
                string = string[a+len(sub_string)-1:]
                i=a+len(sub_string)-1
        return cnt

def while_count_substring(string, sub_string):
        cnt = 0
        j=0
        while(True):
            j=j+1
            print(j)
            if(sub_string in string): 
                cnt = cnt + 1
                a = string.index(sub_string)
                string = string[a+len(sub_string)-1:]
            else:
                 break
        return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = while_count_substring(string, sub_string)
    print(count)