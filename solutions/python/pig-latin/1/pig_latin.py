def translate_word(text):
    vowels = "aeiou"
    
    if text[0] in vowels or text[:2] == "xr" or text[:2] == "yt":
        return text + "ay"
    
    split = 0
    while split < len(text) and text[split] not in vowels:
        if text[split] == "y" and split > 0:
            break
        split += 1
    
    if split > 0 and text[split - 1:split + 1] == "qu":
        split += 1
    
    return text[split:] + text[:split] + "ay"

def translate(text):
    return " ".join(translate_word(word) for word in text.split())
