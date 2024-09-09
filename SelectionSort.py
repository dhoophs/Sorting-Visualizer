import time
import random
import matplotlib.pyplot as plt

numbers = []
size = 100
gap = 4


def swap(xp, yp):
    return yp, xp


def selectionsort(numbers):
    for i in range(size - 1):

        
        min_index = i

        for j in range(i + 1, size):
            if numbers[j] < numbers[min_index]:
                min_index = j

        
        numbers[min_index], numbers[i] = swap(numbers[min_index], numbers[i])

        
        plt.bar([i for i in range(len(numbers))], numbers)
        plt.show(block=False)
        plt.pause(0.1)
        plt.clf()


def main():

    
    for i in range(1, size + 1):
        numbers.append(i)

    
    random.seed(time.time())
    random.shuffle(numbers)


    plt.bar([i for i in range(len(numbers))], numbers)
    plt.show(block=False)
    plt.pause(0.1)
    plt.clf()

    
    selectionsort(numbers)

    for i in range(size):
        print(numbers[i], end=" ")
    print()

    
    time.sleep(5)

if __name__ == "__main__":
    main()
