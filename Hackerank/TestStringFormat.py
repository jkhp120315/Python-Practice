def print_formatted(number):
    width = len(bin(number)[2:])
    a = [ joinstring(i,width)  for i in range(1,number+1)] 
    print("\n".join(a))

def joinstring(number,width):
    
    return str(number).rjust(width) + " " + oct(number)[2:].rjust(width) + " " + hex(number)[2:].upper().rjust(width) + " " + bin(number)[2:].rjust(width)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)