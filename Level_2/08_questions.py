'''
Problem 8 
Question : Write a loop program to print the two-digit even numbers whose sum of digits is 6. 
Testcase: Output: 24 42 60'''




def even_numbers_with_digit_sum_6():
    result = []

    for i in range(10, 100):
        if i % 2 == 0:
            tens = i // 10
            ones = i % 10

            if tens + ones == 6:
                result.append(i)

    return result

print(even_numbers_with_digit_sum_6())