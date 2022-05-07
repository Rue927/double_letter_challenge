def double_letters(string):
    for letter in range(len(string)-1 ):
        letter1 = string[letter]
        letter2 = string[letter + 1]
        
        if letter1 == letter2:
            return True
    return False      