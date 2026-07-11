def is_valid(isbn):
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    total = 0
    for i, char in enumerate(isbn):
        weight = 10 - i
        if char == "X" and i == 9:
            total += 10
        elif char.isdigit():
            total += int(char) * weight
        else:
            return False
    return total % 11 == 0
        
