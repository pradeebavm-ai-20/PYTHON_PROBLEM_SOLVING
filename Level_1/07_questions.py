''' Problem 7
Question: Get a two-digit number from user and print the ten's digit.
Testcase:
Input: 45 → Output: 4
Input: 56 → Output: 5
'''


def get_tens(num):
    return num // 10

num = int(input("Enter two-digit number: "))
print(get_tens(num))