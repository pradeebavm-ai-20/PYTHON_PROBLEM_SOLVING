'''Problem 5
Question: Get a three-digit number from the user and print the digit in the hundred's
position.
Testcase:
Input: 738 → Output: 7'''

def hundreds_digit(num):
    return num // 100

num = int(input("Enter a three-digit number: "))
print(hundreds_digit(num))