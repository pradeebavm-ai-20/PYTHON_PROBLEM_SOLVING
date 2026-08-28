'''Problem 11
Question: Get a two-digit number from user and print sum the digits.
Testcase:
Input: 56 → Output: 11
Input: 69 → Output: 15'''

num = int(input("Enter a two-digit number: "))
ones = num % 10
tens = num // 10
sum_of_digits = ones + tens
print("The sum of the digits is:", sum_of_digits)