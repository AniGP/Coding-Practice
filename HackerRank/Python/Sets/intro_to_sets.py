def average(array):
    # your code goes here
    array_set = set(array)
    array_sum = 0
    
    for i in array_set:
        array_sum += i
    return array_sum/len(array_set)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)