def check_happy(n):
    while n != 1 and n != 4:
        total = 0

        while n > 0:
            digit = n % 10
            total = total + digit ** 2
            n = n // 10

        n = total

    return n == 1