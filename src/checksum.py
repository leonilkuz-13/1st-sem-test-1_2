def modulo11Checksum(ISBNNumber: str):

    digits = [int(char) for char in ISBNNumber if char.isdigit()]

    checkDigit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10
        digit = digits[i]
        total += digit * weight

    checksum = total + checkDigit
    return checksum % 11 == 0
