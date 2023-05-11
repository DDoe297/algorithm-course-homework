from typing import Dict, List


def findMaximumLengthSubarray(array: List[int], x: int) -> List[int]:
    d: Dict[int, int] = {}
    d[0] = -1
    sum: int = 0
    length: int = 0
    ending_index: int = -1
    for i, num in enumerate(array):
        sum += num
        if sum not in d:
            d[sum] = i
        if sum - x in d and length < i - d[sum - x]:
            length = i - d[sum - x]
            ending_index = i
    return array[ending_index-length+1:ending_index+1]


print(findMaximumLengthSubarray([-10, -8, 3, -7, 13,-5,14,-1, -10,12], 15))
