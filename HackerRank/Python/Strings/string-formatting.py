def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        
        b = bin(i)[2:]
        d = str(i)
        o = oct(i)[2:]
        h = hex(i)[2:].upper()
        
        print(f'{d:>{width}} {o:>{width}} {h:>{width}} {b:>{width}}')

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)