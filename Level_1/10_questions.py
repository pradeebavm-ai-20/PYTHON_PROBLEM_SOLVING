'''Problem 10
Question: Get a three-digit number from user and print the ten's digit.
Testcase:
Input: 456 → Output: 5
Input: 569 → Output: 6 ''' 


num = int(input("Enter a three-digit number: "))
tens = (num // 10) % 10
print("The ten's digit is:", tens)