'''Question: Get a two-digit number from user and print the one's digit.

Testcase:
Input: 45 → Output: 5
Input: 56 → Output: 6'''


def get_ones(num):
    return num % 10

num = int(input("Enter two-digit number: "))
print(get_ones(num))