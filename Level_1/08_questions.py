''' Problem 8
Question: Get a three-digit number from user and print the one's digit.
Testcase:
Input: 456 → Output: 6
Input: 569 → Output: 9'''


def get_ones(num):
    return num % 10

num = int(input("Enter three-digit number: "))
print(get_ones(num))