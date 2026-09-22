'''
Problem 7 
Question: Write a loop program to print the two-digit odd numbers whose sum of digits is 7. 
Testcase: Output: 25 43 61'''





def numbers_with_digit_sum_7():
    result = []

    for i in range(10, 100):
        if i % 2 != 0:
            tens = i // 10
            ones = i % 10

            if tens + ones == 7:
                result.append(i)

    return result

print(numbers_with_digit_sum_7())