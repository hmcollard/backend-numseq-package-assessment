def fib(n):
    """Returns num in fibinachi sequence"""
    if n >= 0:
        result1 = 0
        result2 = 1
        for _ in range(n-1):
            result3 = result1 + result2
            result2 = result1
            result1 = result3
    return result3
