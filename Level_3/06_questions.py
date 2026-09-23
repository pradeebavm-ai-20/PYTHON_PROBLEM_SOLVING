'''Problem 6
Question: Get a number from user and reverse that number.
Testcase:
Input: 123 → Output: 321
Input: 56789 → Output: 98765'''

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("Enter a number: "))
print(reverse_number(num))