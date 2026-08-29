'''Problem 4
Question: Get a number from user and divide by the number by 6 and print the quotient.
Testcase:
Input: 45 → Output: 7
Input: 143 → Output: 23 '''




def quo(num):
    return num // 6

num = int(input("Enter number: "))
print(quo(num))