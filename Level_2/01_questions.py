'''Problem 1
Question: Write a loop program to print 1 to 5 one by one.
Testcase:
Output:
1
2
3
4
5'''

def print_numbers():
    result = []

    for i in range(1, 6):
        result.append(i)

    return result

print(print_numbers())