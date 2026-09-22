'''Problem 4 
Question: Write a loop program to print the sum of 6 to 1. 
Testcase: 
Output: 21
'''




def sum_numbers():
    total = 0

    for i in range(6, 0, -1):
        total += i

    return total

print(sum_numbers())