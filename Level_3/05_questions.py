'''Problem 5
Question: Get a number from user and count the number of zeros in that number.
Testcase:
Input: 100 → Output: 2
Input: 1060030 → Output: 4'''

def count_zeros(num):
    count = 0

    while num > 0:
        digit = num % 10

        if digit == 0:
            count += 1

        num = num // 10

    return count

num = int(input("Enter a number: "))
print(count_zeros(num))