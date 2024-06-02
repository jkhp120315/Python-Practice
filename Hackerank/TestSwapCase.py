def swap_case(s):
    a = [i.lower() if i.isupper() else i.upper() for i in s ]
    print("".join(a))
    return

if __name__ == '__main__':
    swap_case('Www.HackerRank.com → wWW.hACKERrANK.COM')
    swap_case('Pythonist 2')