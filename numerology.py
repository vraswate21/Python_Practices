def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
        if number == 0 and sum > 9:
            number = sum
            sum = 0
    return sum

sum_digits(8899)
