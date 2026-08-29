""" Problem 1
Question: Get a number from user and add 2 to that number and print the result.
Testcase:
Input: 45 → Output: 47
Input: 56789 → Output: 56791

"""


def add(num):
    return num + 2

try:
    num = int(input("Enter number: "))
    print(add(num))
except ValueError:
    print("Please enter a valid number.")