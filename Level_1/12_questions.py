''' Problem 12
Question: Get a three-digit number from user and print sum the digits.
Testcase:
Input: 562 → Output: 13
Input: 469 → Output: 19'''

num = int(input("Enter a three-digit number: "))
ones = num % 10
tens = (num // 10) % 10
hundreds = num // 100
sum_of_digits = ones + tens + hundreds
print("The sum of the digits is:", sum_of_digits)