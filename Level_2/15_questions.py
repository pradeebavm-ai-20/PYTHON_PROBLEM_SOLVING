'''Problem 15 
Question: Write a program to get a number from the user. If the first digit is even, print the same number. If the first digit is odd, subtract 1 from the first digit and print the number. 
Testcase: 
Input: 123456 → Output: 023456 
Input: 96895439 → Output: 86895439 
Input: 675 → Output: 675 
Input: 575 → Output: 475
'''
def modify_first_digit(num):
    num = str(num)

    first_digit = int(num[0])

    if first_digit % 2 == 0:
        return num

    first_digit -= 1

    return str(first_digit) + num[1:]
num = int(input("Enter a number: "))
print(modify_first_digit(num))