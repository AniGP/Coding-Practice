if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    sorted_list = sorted(list(arr))
    answer = [ans for ans in sorted_list if ans != max(sorted_list)]
    
    print(max(answer))