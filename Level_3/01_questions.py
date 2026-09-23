'''
Problem 1 
Question: Get a number from user and add 2 to that number and print the result. Write your code inside the function. Testcase: 
Input: 45 → Output: 47 
Input: 56789 → Output: 56791'''

from operator import add


def add_two(num):
    return num + 2

num = int(input("Enter a number: "))
print(add_two(num))