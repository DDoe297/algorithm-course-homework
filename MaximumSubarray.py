def maxValue(array):
    l = [0 for i in array]
    r = [0 for i in array]
    n = len(array)
    st = []
    for i in range(1, n):
        while (len(st) and array[st[-1]] >= array[i]):
            st.pop()
        if (len(st)):
            l[i] = st[len(st) - 1] + 1
        else:
            l[i] = 0
        st.append(i)
    st = []
    for i in range(n-1, -1, -1):
        while (len(st) and array[st[-1]] >= array[i]):
            st.pop()
        if (len(st)):
            r[i] = st[-1] - 1
        else:
            r[i] = n - 1
        st.append(i)
    maxProduct = 0
    for i in range(n):
        if l[i] == 0:
            tempProduct = (array[i] * r[i])
        else:
            tempProduct = (array[i] * (r[i] - (l[i] - 1)))
        if tempProduct > maxProduct:
            left = l[i]
            right = r[i]+1
            maxProduct = tempProduct

    return array[left:right], maxProduct


a = [1, 2, 3, 4, 5, 6, 7]
print(maxValue(a))
