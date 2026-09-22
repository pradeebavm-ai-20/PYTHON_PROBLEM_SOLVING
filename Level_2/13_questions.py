'''Problem 13 
Question: Write a program to get a number from the user and print the reverse of that number. 
Testcase: 
Input: 123456 → Output: 654321 
Input: 76895439 → Output: 93459867 
Input: 675 → Output: 576
'''
def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse
num = int(input("Enter a number: "))
print(reverse_number(num))