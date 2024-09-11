import time
import random
import matplotlib.pyplot as plt

numbers = []
size = 100


def merge(numbers, left, mid, right):

    left_array = numbers[left:mid + 1]
    right_array = numbers[mid + 1:right + 1]

    i = 0
    j = 0
    k = left


    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            numbers[k] = left_array[i]
            i += 1
        else:
            numbers[k] = right_array[j]
            j += 1
        k += 1


    while i < len(left_array):
        numbers[k] = left_array[i]
        i += 1
        k += 1


    while j < len(right_array):
        numbers[k] = right_array[j]
        j += 1
        k += 1


    plt.bar([i for i in range(len(numbers))], numbers)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()


def mergesort(numbers, left, right):
    if left < right:
        
        mid = (left + right) // 2

        mergesort(numbers, left, mid)
        mergesort(numbers, mid + 1, right)

        merge(numbers, left, mid, right)


def main():

    for i in range(1, size + 1):
        numbers.append(i)

    random.seed(time.time())
    random.shuffle(numbers)

    plt.bar([i for i in range(len(numbers))], numbers)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    mergesort(numbers, 0, size - 1)

    for i in range(size):
        print(numbers[i], end=" ")
    print()

    time.sleep(5)


if __name__ == "__main__":
    main()
