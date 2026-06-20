def finding_factors(number):
    factors = []
    
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
        
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors

def classify(number):
    aliquot_sum = 0
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = finding_factors(number)
    for factor in factors:
        aliquot_sum += factor
    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    else:
        return "deficient"
    
    
        