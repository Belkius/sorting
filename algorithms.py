import numbers


#array, length
def selection(array, length):
    for i in range(0, length):
        minimum = i
        for j in range(0 + i, length):
            if array[minimum] > array[j]:
                minimum = j
        numbers.swap(array, i, minimum)


#array, length
def bubble(array, length):
    for i in range (0, length):
        for j in range (0, length - i - 1):
            if array[j] > array[j + 1]:
                numbers.swap(array, j, j + 1)


#array, 0, length - 1
def quick(array, low, high):
    if low < high:
        pivot = array[high]
        pointer = low - 1
        for i in range(low, high):
            if array[i] <= pivot:
                pointer = pointer + 1
                numbers.swap(array, pointer, i)
        numbers.swap(array, pointer + 1, high)

        quick(array, low, pointer)
        quick(array, pointer + 2, high)


def heapify(array, length, index):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < length and array[left] > array[largest]:
        largest = left

    if right < length and array[right] > array[largest]:
        largest = right

    if largest != index:
        numbers.swap(array, index, largest)
        heapify(array, length, largest)


#array, length
def heap(array, length):
    for i in range(length//2, -1, -1):
        heapify(array, length, i)

    for i in range(length - 1, 0, -1):
        numbers.swap(array, 0, i)
        heapify(array, i, 0)


#array, length
def insertion(array, length):
    for i in range(1, length):
        key = array[i]
        for j in range(i - 1, -1, -1):
            if key < array[j]:
                numbers.swap(array, j + 1, j)


#array, length
def merge(array, length):
    if length > 1:
        middle = length//2
        low = array[:middle]
        high = array[middle:]

        merge(low, len(low))
        merge(high, len(high))

        low_count = high_count = 0

        for i in range(length):
            if low_count < len(low) and high_count < len(high):
                if low[low_count] <= high[high_count]:
                    array[high_count + low_count] = low[low_count]
                    low_count += 1
                else:
                    array[high_count + low_count] = high[high_count]
                    high_count += 1
            elif low_count < len(low):
                array[high_count + low_count] = low[low_count]
                low_count += 1
            else:
                array[high_count + low_count] = high[high_count]
                high_count += 1


def merge2(array, length):
    if length > 1:
        middle = length//2
        low = array[:middle]
        high = array[middle:]

        merge(low, len(low))
        merge(high, len(high))

        low_count = high_count = 0

        while low_count < len(low) and high_count < len(high):
            if low[low_count] <= high[high_count]:
                array[high_count + low_count] = low[low_count]
                low_count += 1
            else:
                array[high_count + low_count] = high[high_count]
                high_count += 1

        while low_count < len(low):
            array[high_count + low_count] = low[low_count]
            low_count += 1

        while high_count < len(high):
            array[high_count + low_count] = high[high_count]
            high_count += 1


#def shell():
