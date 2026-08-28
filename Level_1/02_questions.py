''' Problem 2
Question: Get a number from user and subtract 5 to that number and print the result.
Testcase:
Input: 45 → Output: 40
Input: 56789 → Output: 56784'''



# exception handling
try:
    num = int(input("Enter the number: "))
    sub = num-5
    print("The number subtract by 5 is:",sub)
except ValueError:
    print("Please enter a valid integer.")