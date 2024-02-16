def count_substring(string, sub_string):
    
    start = 0
    end = len(string) - len(sub_string)
    count = 0
    
    if end < 0:
        return 0
        
    while start < end:
        
        start = string.find(sub_string, start) + 1
        
        if start < 1:
            break
        count += 1
    
