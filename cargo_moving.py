from typing import Dict, Tuple


def F(n: int, m: int, k: int, memo: Dict[Tuple[int, int], int]) -> int:
    if (n, k) in memo:
        return memo[(n, k)]
    number_of_ways: int = 0
    if n == 0:
        return 1
    if k == 0:
        return 1
    for i in range(1, m+1):
        if i<=n:
            number_of_ways += F(n-i, m, k-1, memo)
    memo[(n, k)] = number_of_ways
    return number_of_ways

print(F(10, 2, 7, {}))
