'''Problem 11 
Question: Write a program to get a number from the user and print the total number of digits in that number. 
Testcase: 
Input: 123456 → Output: 6 
Input: 76895439 → Output: 8 
Input: 675 → Output: 3
'''
def count_digits(num):
    count = 0

    while num > 0:
        num = num // 10
        count += 1

    return count

num = int(input("Enter a number: "))
print(count_digits(num))