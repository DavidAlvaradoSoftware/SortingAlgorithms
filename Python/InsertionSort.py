import array
import argparse
from numpy import random



def main():
    parser = argparse.ArgumentParser(description='Sorts a randomly generated array of integers')
    parser.add_argument('-l', '--length', type=int, help ='length of array to be generated')
    args = parser.parse_args()

    if args.length is None:
        print("Length of the randomly generated array was not specified, default value of 10 will be used.")
        args.length = 10

    unsorted_array = random.randint(500, size=(args.length))
    print("Unsorted Array: ", unsorted_array)
    
    insertion_sort(unsorted_array)

def insertion_sort(unsorted_array):
    for number in range(1,len(unsorted_array)):
        value = unsorted_array[number]
        hole = number
        while hole > 0 and unsorted_array[hole-1] > value:
            unsorted_array[hole] = unsorted_array[hole-1]
            hole = hole - 1
        unsorted_array[hole] = value

    print("Insertion Sorted Array: ", unsorted_array)


if __name__ == "__main__":
    main()