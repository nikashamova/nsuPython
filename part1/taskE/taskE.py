#import no_standart_sort


def quick_sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quick_sort(less)+equal+quick_sort(greater)
    else:
        return array


def quick_sort_iterative(list_, left, right):
    temp_stack = []
    temp_stack.append((left, right))

    while temp_stack:
        pos = temp_stack.pop()
        right, left = pos[1], pos[0]
        piv = partition(list_, left, right)
        if piv - 1 > left:
            temp_stack.append((left, piv - 1))
        if piv + 1 < right:
            temp_stack.append((piv + 1, right))
    return list_


def partition(list_, left, right):
    piv = list_[left]
    i = left + 1
    j = right
    while 1:
        while i <= j and list_[i] <= piv:
            i += 1
        while j >= i and list_[j] >= piv:
            j -= 1
        if j <= i:
            break
        list_[i], list_[j] = list_[j], list_[i]
    list_[left], list_[j] = list_[j], list_[left]
    return j


def merge(a, left, mid, right):
    copy_list = []
    i, j = left, mid + 1
    ind = left
    while ind < right + 1:
        if i > mid:
            copy_list.append(a[j])
            j += 1
        elif j > right:
            copy_list.append(a[i])
            i += 1
        elif a[j] < a[i]:
            copy_list.append(a[j])
            j += 1
        else:
            copy_list.append(a[i])
            i += 1
        ind += 1

    ind = 0
    for x in (range(left, right + 1)):
        a[x] = copy_list[ind]
        ind += 1


def merge_sort_iterative(list_, left, right):
    factor = 2
    temp_mid = 0
    while 1:
        index = 0
        left = 0
        right = len(list_) - (len(list_) % factor) - 1
        mid = (factor / 2) - 1

        while index < right:
            temp_left = index
            temp_right = temp_left + factor - 1
            mid2 = (temp_right + temp_left) // 2
            merge(list_, temp_left, mid2, temp_right)
            index = (index + factor)

        if len(list_) % factor and temp_mid != 0:
            merge(list_, right + 1, temp_mid, len(list_) - 1)
            mid = right
        factor *= 2
        temp_mid = right

        if factor > len(list_):
            mid = right
            right = len(list_) - 1
            merge(list_, 0, mid, right)
            break
    return list_

file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

line = file_input.readline().split()
array = [int(x) for x in line]

result = quick_sort(array)

for r in result:
    file_output.write(str(r) + " ")
file_output.write("\n")

file_input.close()
file_output.close()

