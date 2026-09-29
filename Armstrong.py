def check_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    return total == original