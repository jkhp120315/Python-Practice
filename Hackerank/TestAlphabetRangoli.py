def print_rangoli(size):
    # your code goes here
    alphabet = [chr(i) for i in range(97,123) ]
    alphabet = alphabet[:size]
    print(alphabet)

    indices = [i for i in range(size)] 
    print(indices[:-1])
    print(indices[::-1])
    indices = indices[:-1] + indices[::-1]

    print(indices)
    for i in indices:
        start_index = i + 1
        #original = alphabet[-start_index:]
        original =  alphabet[len(alphabet)-start_index:]
        reverse = original[:-len(original):-1]
        row = reverse + original
        row = "-".join(row)
        width = size * 4 - 3        
        print(row.center(width,"-"))        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)