def check_harshad(n):
    original = n
    digit_sum = 0

    while n > 0:
        digit = n % 10
        digit_sum = digit_sum + digit
        n = n // 10

    return original % digit_sum == 0