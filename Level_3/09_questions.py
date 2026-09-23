'''Problem 9
Question: Get a two-digit number from user and swap the digits.
Testcase:
Input: 34 → Output: 43
Input: 56 → Output: 65
'''

def swap_digits(num):
    tens = num // 10
    ones = num % 10

    return ones * 10 + tens

num = int(input("Enter a two-digit number: "))
print(swap_digits(num))