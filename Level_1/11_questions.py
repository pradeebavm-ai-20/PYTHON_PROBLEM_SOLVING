'''Problem 11
Question: Get a two-digit number from user and print sum the digits.
Testcase:
Input: 56 → Output: 11
Input: 69 → Output: 15'''

def sum_digits(num):
    ones = num % 10
    tens = num // 10

    return ones + tens


num = int(input("Enter two-digit number: "))
print(sum_digits(num))