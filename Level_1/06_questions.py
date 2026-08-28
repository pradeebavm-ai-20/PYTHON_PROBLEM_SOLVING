'''Question: Get a two-digit number from user and print the one's digit.

Testcase:
Input: 45 → Output: 5
Input: 56 → Output: 6'''


num = int(input("Enter a two-digit number: "))
ones = num % 10
print("The one's digit is:", ones)