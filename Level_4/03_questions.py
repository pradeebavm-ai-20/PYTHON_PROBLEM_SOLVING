'''Problem 3
Question: Get a three-digit number from the user and print the digit in the one's position.
Testcase:
Input: 738 → Output: 8'''

def ones_digit(num):
    return num % 10

num = int(input("Enter a three-digit number: "))
print(ones_digit(num))