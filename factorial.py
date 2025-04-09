def rec_sum(n):
    if n ==0:
        return 0
    return (n % 10) + rec_sum (n // 10)
print(rec_sum(1234))