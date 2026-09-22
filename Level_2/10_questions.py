'''
Problem 10 
Question: Write a loop program to print the sum of two-digit odd numbers whose ten's digit is 7. 
Testcase: Output: 375'''


def sum_numbers_starting_with_7():
    total = 0

    for i in range(70, 80):
        if i % 2 != 0:
            total += i

    return total

print(sum_numbers_starting_with_7())