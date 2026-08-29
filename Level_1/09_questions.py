'''Problem 9
Question: Get a three-digit number from user and print the hundred's digit.
Testcase:
Input: 456 → Output: 4
Input: 569 → Output: 5'''


def get_hundreds(num):
    return num // 100

num = int(input("Enter three-digit number: "))
print(get_hundreds(num))