def mutate_string(string, position, character):
    
    l = list(string)
    l[position] = character
    new_string = ''.join(l)
    
    return new_string