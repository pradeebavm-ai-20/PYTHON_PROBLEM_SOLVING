'''Problem 13
Question: Get a two-digit number from user and print the reverse of the number.
Testcase:
Input: 56 → Output: 65
Input: 59 → Output: 9'''

def reverse_number(num):
    ones = num % 10
    tens = num // 10

    return ones * 10 + tens


num = int(input("Enter two-digit number: "))
print(reverse_number(num))