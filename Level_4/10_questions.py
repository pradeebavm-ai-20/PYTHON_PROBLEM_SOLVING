'''Problem 10
Question: Get a three-digit number from the user and print the sum of all digits.
Testcase:
Input: 738 → Output: 18'''

def sum_three_digits(num):
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = num // 100

    return ones + tens + hundreds

num = int(input("Enter a three-digit number: "))
print(sum_three_digits(num))