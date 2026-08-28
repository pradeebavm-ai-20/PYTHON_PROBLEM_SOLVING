'''Problem 13
Question: Get a two-digit number from user and print the reverse of the number.
Testcase:
Input: 56 → Output: 65
Input: 59 → Output: 9'''

num = int(input("Enter a number: "))

reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10

print("The reverse of the number is:", reverse_num)