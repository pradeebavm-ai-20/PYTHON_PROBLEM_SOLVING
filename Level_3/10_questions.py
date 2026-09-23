'''Problem 10
Question: Get a number from user, find the number of digits, and print it.
Testcase:
Input: 34678 → Output: 5
Input: 12345678 → Output: 8'''


def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10


    return count

num = int(input("Enter a number: "))
print(count_digits(num))