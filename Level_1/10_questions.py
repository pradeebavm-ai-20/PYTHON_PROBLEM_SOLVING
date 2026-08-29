'''Problem 10
Question: Get a three-digit number from user and print the ten's digit.
Testcase:
Input: 456 → Output: 5
Input: 569 → Output: 6 ''' 

def get_tens(num):
    return (num // 10) % 10

num = int(input("Enter three-digit number: "))
print(get_tens(num))