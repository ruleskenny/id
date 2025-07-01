# Simple Roman numeral calculator

# Map of Roman numerals to integers
roman_to_int_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Ordered list for integer to Roman conversion
int_to_roman_list = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]

def roman_to_int(roman):
    """Convert Roman numeral to integer."""
    i = 0
    total = 0
    while i < len(roman):
        if i + 1 < len(roman) and roman_to_int_map[roman[i]] < roman_to_int_map[roman[i + 1]]:
            total += roman_to_int_map[roman[i + 1]] - roman_to_int_map[roman[i]]
            i += 2
        else:
            total += roman_to_int_map[roman[i]]
            i += 1
    return total

def int_to_roman(number):
    """Convert integer to Roman numeral."""
    result = []
    for value, numeral in int_to_roman_list:
        while number >= value:
            result.append(numeral)
            number -= value
    return ''.join(result)

# Supported operations
operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b  # integer division, Roman numerals have no fractions
}

def calculate(roman1, roman2, op):
    """Perform calculation on two Roman numerals."""
    if op not in operators:
        raise ValueError(f"Unsupported operator: {op}")
    a = roman_to_int(roman1)
    b = roman_to_int(roman2)
    result = operators[op](a, b)
    if result <= 0:
        raise ValueError("Result cannot be represented as a Roman numeral")
    return int_to_roman(result)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python roman_calculator.py ROMAN1 OPERATOR ROMAN2")
        print("Example: python roman_calculator.py X + V")
        sys.exit(1)
    r1, op, r2 = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        result = calculate(r1, r2, op)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
