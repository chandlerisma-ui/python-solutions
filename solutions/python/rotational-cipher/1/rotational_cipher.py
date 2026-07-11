def shift_char(char, key):
    if char.isupper():
        return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    else:
        return chr((ord(char) - ord('a') + key) % 26 + ord('a'))

def rotate(text, key):
    result = ""
    for letter in text:
        if letter.isalpha():
            result += shift_char(letter, key)
        else:
            result += letter
    return result
                
                
            
        
