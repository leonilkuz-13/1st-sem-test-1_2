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


print("Exit - -1")
print("To enter, enter any number")
string = input()
while True:
    print("enter ISBN_number or came out")
    if string == "-1":
        print("you came out")
        break
    string = input()
    if modulo11_checksum(string):
        print("correct")
    else:
        print("incorrect")
