def sort(array, index):
    if index == len(array):
        return
    min_index = array.index(min(array[index:]))
    array[min_index], array[index] = array[index], array[min_index]
    sort(array, index + 1)

array = [145, 117, 92, 176, 51, 35, 22, 12, 5, 1, 70]
sort(array,0)
print(array)
