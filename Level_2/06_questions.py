'''Problem 6 
Question: 
Write a loop program to print the two-digit odd numbers below 20. 
Testcase: 
Output: 11 13 15 17 19
'''


def two_digit_odd_numbers():
    result = []

    for i in range(10, 20):
        if i % 2 != 0:
            result.append(i)

    return result

print(two_digit_odd_numbers())