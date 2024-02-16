def swap_case(s):
    
    ans = ""
    
    for letter in s:
        
        if letter.isalpha():
            
            if letter == letter.lower():
                ans = ans + letter.upper()
                
            else:
                ans = ans + letter.lower()
        else:
            ans = ans + letter
                
    return ans