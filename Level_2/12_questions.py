'''Problem 12 
Question: Write a program to get a number from the user and print the sum of all digits. 
Testcase: 
Input: 123456 → Output: 21 
Input: 76895439 → Output: 51 
Input: 675 → Output: 18'''

def sum_digits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    return total
num = int(input("Enter a number: "))
print(sum_digits(num))