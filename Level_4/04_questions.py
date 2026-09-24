'''Problem 4
Question: Get a three-digit number from the user and print the digit in the ten's position.
Testcase:
Input: 738 → Output: 3'''

def tens_digit(num):
    return (num // 10) % 10

num = int(input("Enter a three-digit number: "))
print(tens_digit(num))