# perform bucket sort on the array and return the sorted array
def bucketSort(array):
   # check the length of the array
    if len(array) == 0:  # check if the input array is empty
        return array  # return the empty array if so

    # step 1: find the minimum and maximum values in the array to determine the number of buckets
    min_value = min(array)
    max_value = max(array)
    bucket_count = len(array)  # set the number of buckets equal to the number of elements

    # create empty buckets as a list of empty lists
    buckets = [[] for _ in range(bucket_count)]

    # step 2: distribute the elements into appropriate buckets
    for num in array:
        # calculate the bucket index based on the current number
        # this formula maps the number to a bucket index between 0 and bucket_count - 1
        index_b = int(((num - min_value) / (max_value - min_value)) * (bucket_count - 1))
        buckets[index_b].append(num)  # append the number to the appropriate bucket

    # step 3: sort each bucket
    for i in range(bucket_count):  # iterate over each bucket
        # sort the current bucket
        buckets[i] = sorted(buckets[i])

    # step 4: put the sorted buckets back into the original array
    sorted_array = []
    for bucket in buckets: # loop through each bucket
        sorted_array.extend(bucket)

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
