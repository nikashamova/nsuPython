#import no_standart_sort


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


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

line = file_input.readline().split()
array = [int(x) for x in line]

result = quick_sort_iterative(array, 0, len(array) - 1)

for r in result:
    file_output.write(str(r) + " ")
file_output.write("\n")

file_input.close()
file_output.close()

