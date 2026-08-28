'''Problem 9
Question: Get a three-digit number from user and print the hundred's digit.
Testcase:
Input: 456 → Output: 4
Input: 569 → Output: 5'''


num = int(input("Enter a three-digit number: "))
hundreds = num // 100
print("The hundred's digit is:", hundreds)