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


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

line = file_input.readline().split()
array = [int(x) for x in line]

result = quick_sort(array)

'''
for r in result:
    result = (str(r) + " ")
file_output.write("\n")
'''

print(*quick_sort(array))

file_input.close()
file_output.close()

