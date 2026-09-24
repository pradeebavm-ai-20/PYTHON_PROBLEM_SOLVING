'''Problem 6
Question: Get a two-digit number from the user and print its reverse.
Testcase:
Input: 73 → Output: 37'''

def reverse_two_digit(num):
    ones = num % 10
    tens = num // 10

    return ones * 10 + tens

num = int(input("Enter a two-digit number: "))
print(reverse_two_digit(num))