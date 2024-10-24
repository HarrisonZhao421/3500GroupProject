# perform insertion sort on the array (sorts the array in place and then returns it)

def insertionSort(array):
    # loop through the array starting from the second element
    for i in range(1, len(array)):
        key = array[i]  # the current element to be compared
        j = i - 1  # the index of the last sorted element

        # move elements of array[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]  # shift the element one position to the right
            j -= 1  # move to the previous element

        # place the key element at its correct position
        array[j + 1] = key
    
    return array  # Return the sorted array

# perform bucket sort on the array and return the sorted array
def bucketSort(array):
   # check the length of the array
    if len(array) == 0:  # check if the input array is empty
        return array  # return the empty array if so

    # step 1: find the maximum value to determine the number of buckets
    max_value = max(array)
    bucket_count = len(array)  # set the number of buckets equal to the number of elements
    # create empty buckets as a list of empty lists
    bucket = [[] for _ in range(bucket_count)]

    # step 2: distribute the elements into appropriate buckets
    for num in array:
        # calculate the bucket index based on the current number
        # this formula maps the number to a bucket index between 0 and bucket_count - 1
        index_b = int((num / max_value) * (bucket_count - 1))
        # append the number to the appropriate bucket
        bucket[index_b].append(num)

    # step 3: sort each bucket using insertion sort
    for i in range(bucket_count):  # iterate over each bucket
        # sort the current bucket using insertion sort
        bucket[i] = insertionSort(bucket[i])

    # step 4: put the sorted buckets back into the original array
    sorted_array = []
    for i in range(bucket_count):  # loop through each bucket
        sorted_array.extend(bucket[i])

    return sorted_array

# example test cases:

# testing with integers
int_array = [1, 20, 23, 32, 40, 11, 5, 8]
sorted_int_array = bucketSort(int_array)
print("Sorted Integer Array is: ")
print(sorted_int_array)

# testing with decimals
decimal_array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_decimal_array = bucketSort(decimal_array)
print("Sorted Decimal Array is: ")
print(sorted_decimal_array)
