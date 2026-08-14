def rebase(input_base, digits, output_base):
    # validate inputs
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # step 1 — convert to base 10 using Horner's method
    base10 = 0
    for digit in digits:
        base10 = base10 * input_base + digit
    
    # handle zero
    if base10 == 0:
        return [0]
    
    # step 2 — convert base 10 to output base
    result = []
    while base10 > 0:
        result.append(base10 % output_base)  # remainder is the digit
        base10 //= output_base               # floor divide strips that layer
    
    # remainders came out last-to-first so reverse
    return result[::-1]


    