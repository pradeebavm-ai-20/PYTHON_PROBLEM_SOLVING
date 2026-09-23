'''Problem 8
Question: Get a number from user and check whether its digits are in ascending order.
Testcase:
Input: 1234 → Output: Yes
Input: 5687 → Output: No'''

def ascending_order(num):
    previous = num % 10
    num = num // 10

    while num > 0:
        current = num % 10

        if current > previous:
            return "No"

        previous = current
        num = num // 10

    return "Yes"

num = int(input("Enter a number: "))
print(ascending_order(num))