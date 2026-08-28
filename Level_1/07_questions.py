''' Problem 7
Question: Get a two-digit number from user and print the ten's digit.
Testcase:
Input: 45 → Output: 4
Input: 56 → Output: 5
'''

num = int(input("Enter a two-digit number: "))
tens = num // 10
print("The ten's digit is:", tens)
