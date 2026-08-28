''' Problem 8
Question: Get a three-digit number from user and print the one's digit.
Testcase:
Input: 456 → Output: 6
Input: 569 → Output: 9'''


num = int(input("Enter a three-digit number: "))
ones = num % 10
print("The one's digit is:", ones)
