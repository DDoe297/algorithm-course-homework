from typing import List, Tuple


def findTriplets(numbers: List[int]) -> List[Tuple[int, int, int]]:
    triplets: List[Tuple[int, int, int]] = []
    numbers.sort()
    i: int = len(numbers) - 1
    while(i >= 0):
        j: int = 0
        k: int = i - 1
        while (j < k):
            if (numbers[i] == numbers[j] + numbers[k]):
                triplets.append((numbers[j], numbers[k], numbers[i]))
                break
            elif (numbers[i] > numbers[j] + numbers[k]):
                j += 1
            else:
                k -= 1
        i -= 1
    return triplets

