'''Problem 8
Question: Get a four-digit number from the user and print its reverse.
Testcase:
Input: 7384 → Output: 4837'''

def reverse_four_digit(num):
    ones = num % 10
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10
    thousands = num // 1000

    return ones * 1000 + tens * 100 + hundreds * 10 + thousands

num = int(input("Enter a four-digit number: "))
print(reverse_four_digit(num))