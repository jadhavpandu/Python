def binary_subtraction(a, b):
    # Ensure a is the longer or equal length string
    if len(a) < len(b):
        a, b = b, a

    # Pad the shorter string with zeros on the left
    b = b.zfill(len(a))

    # Initialize variables
    result = ""
    borrow = 0

    # Perform the subtraction from right to left
    for i in range(len(a) - 1, -1, -1):
        digit_a = int(a[i])
        digit_b = int(b[i])

        # Perform subtraction with borrow
        sub = digit_a - digit_b - borrow

        if sub == 0:
            result = "0" + result
            borrow = 0
        elif sub == 1:
            result = "1" + result
            borrow = 0
        elif sub == -1:
            result = "1" + result
            borrow = 1
        elif sub == -2:
            result = "0" + result
            borrow = 1

    # Remove leading zeros in the result
    result = result.lstrip("0")

    # Return '0' if the result is empty (when both inputs are the same)
    return result if result != "" else "0"

# Example usage:
a = "1101"  # 13 in decimal
b = "101"   # 5 in decimal

print(binary_subtraction(a, b))  # Output: "1000" (8 in decimal)
