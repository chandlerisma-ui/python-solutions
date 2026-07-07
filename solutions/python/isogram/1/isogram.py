def is_isogram(phrase):
    letter_count = {}
    phrase = phrase.lower().replace('-','').replace(' ', '')
    for letter in phrase:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for count in letter_count.values():
        if count > 1:
            return False
    return True
        
        
