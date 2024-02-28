cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    
    fib = []
    
    if n == 1:
        fib = [0]
        
    elif n == 2:
        fib = [0, 1]
        
    elif n > 2:
        
        fib = [0, 1]
        
        for i in range(n-2):
            
            fib.append(fib[i] + fib[i+1])
    
    return fib
        
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))