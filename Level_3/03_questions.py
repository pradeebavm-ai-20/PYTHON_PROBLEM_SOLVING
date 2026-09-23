'''Problem 3
Question: Get a number from user and check whether the sum of digits is 14, then print
the result.
Testcase:
Input: 59 → Output: Sum of Digits is 14
Input: 123 → Output: Sum of Digits is not 14'''


def check_digit_sum(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    if total == 14:
        return "Sum of Digits is 14"
    else:
        return "Sum of Digits is not 14"

num = int(input("Enter a number: "))
print(check_digit_sum(num))    