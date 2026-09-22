'''Problem 14 
Question: Write a program to get a number from the user and interchange the first and last digits, then print the result. Testcase: 
Input: 123456 → Output: 623451 
Input: 76895439 → Output: 96895437 
Input: 675 → Output: 576
'''
def interchange_first_last(num):
    num = str(num)

    if len(num) == 1:
        return num

    result = num[-1] + num[1:-1] + num[0]

    return result
num = int(input("Enter a number: "))
print(interchange_first_last(num))