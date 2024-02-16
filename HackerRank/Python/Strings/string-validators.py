if __name__ == '__main__':
    s = input()
    
    print('True' if any(letter.isalnum() for letter in s) else 'False')
    print('True' if any(letter.isalpha() for letter in s) else 'False')
    print('True' if any(digit.isdigit() for digit in s) else 'False')
    print('True' if any(letter.islower() for letter in s) else 'False')
    print('True' if any(letter.isupper() for letter in s) else 'False') 
