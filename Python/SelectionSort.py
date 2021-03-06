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
    
    selection_sort(unsorted_array)

def selection_sort(unsorted_array):
    array_length = len(unsorted_array)

    for index in range(array_length):
        for sub_index in range(index, array_length):
            if unsorted_array[index] > unsorted_array[sub_index]:
                current_element = unsorted_array[index]
                unsorted_array[index] = unsorted_array[sub_index]
                unsorted_array[sub_index] = current_element

    print("Selection Sorted Array: ", unsorted_array)



if __name__ == "__main__":
    main()
