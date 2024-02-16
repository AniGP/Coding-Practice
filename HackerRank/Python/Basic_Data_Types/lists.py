if __name__ == '__main__':
    N = int(input())
    list = []
    
    for i in range(N):

        op = input().split()
        
        if (op[0]=='insert'): 
            list.insert(int(op[1]), int(op[2]))
            
        elif (op[0]=='print'): 
            print(list)
            
        elif (op[0]=='remove'): 
            list.remove(int(op[1]))
            
        elif (op[0]=='append'): 
            list.append(int(op[1]))
            
        elif (op[0]=='sort'): 
            list.sort()
            
        elif (op[0]=='pop'): 
            list.pop()
            
        elif (op[0]=='reverse'): 
            list.reverse()