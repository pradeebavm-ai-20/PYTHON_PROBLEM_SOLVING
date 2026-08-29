'''
Problem 14
Question: Get a three-digit number from user and print the reverse of the number.
Testcase:
Input: 561 → Output: 165
Input: 859 → Output: 958
'''
  


def reverse(num):
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num = num // 10
        
    return reverse_num

num = int(input("Enter a three-digit number: "))

reversed = reverse(num)
print("The reverse of the number is:", reversed)