def modulo11_checksum(isbn_number: str):
    def correct_number(isbn_number):
        digits = []
        for i in isbn_number:
            if i.isdigit():
                digits.append(int(i))
            elif i.upper() == "X" and len(digits) == 9:
                digits.append(10)
            elif i != "-":
                return None
        return digits if len(digits) == 10 else None

    digits = correct_number(isbn_number)
    if digits is None:
        return False

    total = 0
    for i in range(9):
        weight = 10 - i
        total += digits[i] * (weight)

    total += digits[-1]

    return total % 11 == 0
