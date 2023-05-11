def power(p,n):
    if n == 0:
        return 1
    half_power = power(p, n // 2)
    if n % 2:
        return p * half_power * half_power
    return half_power * half_power
