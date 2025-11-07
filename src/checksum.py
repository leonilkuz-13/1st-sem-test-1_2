def modulo11_checksum(isbn_number: str):
    digits = [int(char) for char in isbn_number if char.isdigit()]

    check_digit = digits[-1]

    total = 0
    for i in range(len(digits) - 1):
        weight = 10
        digit = digits[i]
        total += digit * weight

    checksum = total + check_digit
    return checksum % 11 == 0
