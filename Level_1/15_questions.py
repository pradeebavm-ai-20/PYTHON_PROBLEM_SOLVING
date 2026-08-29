'''Problem 15
Question: Get a four-digit number from user and only reverse the first two digits of the number,
then print the number.
Testcase:
Input: 9561 → Output: 9516
Input: 3859 → Output: 3895'''

def reverse_last_two(num):
    last = num % 100
    reverse = (last % 10) * 10 + (last // 10)
    return (num // 100) * 100 + reverse

num = int(input("Enter number: "))
print(reverse_last_two(num))