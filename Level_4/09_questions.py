'''Problem 9
Question: Get a two-digit number from the user and print the sum of all digits.
Testcase:
Input: 78 → Output: 15'''

def sum_two_digits(num):
    ones = num % 10
    tens = num // 10

    return ones + tens

num = int(input("Enter a two-digit number: "))
print(sum_two_digits(num))