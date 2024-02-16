if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    input_tuple = tuple(integer_list)
    result = hash(input_tuple)
    print(result)