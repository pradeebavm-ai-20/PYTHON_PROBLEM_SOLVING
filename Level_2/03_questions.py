'''Problem 3 
Question: 
Write a loop program to print the sum of 1 to 5. 
Testcase: 
Output: 15
'''





def sum_numbers():
    total = 0

    for i in range(1, 6):
        total += i

    return total

print(sum_numbers())