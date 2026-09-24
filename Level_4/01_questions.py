'''Problem 1
Question: Get a two-digit number from the user and print the digit in the one's position.
Testcase:
Input: 78 → Output: 8'''

def ones_digit(num):
    return num % 10

num = int(input("Enter a two-digit number: "))
print(ones_digit(num))