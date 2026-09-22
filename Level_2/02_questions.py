'''
Problem 2 
Question: Write a loop program to print 5 to 1 one by one. 
Testcase: Output: 5 4 3 2 1
'''
def print_reverse_numbers():
    result = []

    for i in range(5, 0, -1):
        result.append(i)

    return result

print(print_reverse_numbers())