'''
Problem 5 
Question: 
Write a loop program to print odd numbers from 1 to 9. 
Testcase: 
Output: 1 3 5 7 9'''




def odd_numbers():
    result = []

    for i in range(1, 10):
        if i % 2 != 0:
            result.append(i)

    return result

print(odd_numbers())