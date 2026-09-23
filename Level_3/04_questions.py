'''Problem 4
Question: Get a number from user and check whether it is prime or not, then print the
result.
Testcase:
Input: 61 → Output: Number is Prime
Input: 1200 → Output: Number is not Prime'''

def check_prime(num):
    if num < 2:
        return "Number is not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Number is not Prime"

    return "Number is Prime "

num = int(input("Enter a number: "))
print(check_prime(num))
