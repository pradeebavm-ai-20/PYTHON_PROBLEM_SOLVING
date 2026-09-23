'''Problem 7
Question: Get two numbers from user and compare them. If they are the same, print
Same; otherwise print Not Same.
Testcase:
Input: 123, 123 → Output: Same
Input: 56789, 12345 → Output: Not Same'''

def compare_numbers(num1, num2):
    if num1 == num2:
        return "Same"
    else:
        return "Not Same"

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(compare_numbers(num1, num2))