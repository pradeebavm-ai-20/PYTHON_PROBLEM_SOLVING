''' Problem 12
Question: Get a three-digit number from user and print sum the digits.
Testcase:
Input: 562 → Output: 13
Input: 469 → Output: 19'''

def sum_digits(num):
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = num // 100

    return ones + tens + hundreds


num = int(input("Enter three-digit number: "))
print(sum_digits(num))