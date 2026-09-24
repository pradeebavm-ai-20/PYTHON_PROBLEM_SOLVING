'''Problem 2
Question: Get a two-digit number from the user and print the digit in the ten's position.
Testcase:
Input: 78 → Output: 7'''

def tens_digit(num):
    return num // 10

num = int(input("Enter a two-digit number: "))
print(tens_digit(num))