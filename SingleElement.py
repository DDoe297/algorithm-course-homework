def finde_single_element(array):
    low = 0
    high = len(array)
    def middle_find(high, low): return (high-low)//2 + low
    while(low < high):
        middle = middle_find(high, low)
        if middle == low or middle==high-1:
            break
        if array[middle] == array[middle-1]:
            if middle % 2:
                low = middle+1
            else:
                high = middle-1
        elif array[middle] == array[middle+1]:
            if middle % 2 == 0:
                low = middle + 2
            else:
                high = middle
        else:
            break
    return array[middle]
