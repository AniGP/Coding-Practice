def split_and_join(line):
    # write your code here
    line = line.split(" ")
    join = "-".join(line)
    
    return join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)