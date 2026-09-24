'''Problem 7
Question: Get a three-digit number from the user and print its reverse.
Testcase:
Input: 738 → Output: 837'''

def reverse_three_digit(num):
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = num // 100

    return ones * 100 + tens * 10 + hundreds

num = int(input("Enter a three-digit number: "))
print(reverse_three_digit(num))