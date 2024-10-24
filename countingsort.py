''' 
*** COUNTING-SORT ***
Explanation:

Steps: 
    - Find the MAX value of the input array (input_arr)
    - Create a new array (count_arr) with length (max + 1) and all elements set to 0
        - Each index corresponds the the possible values that may be in the input array
    - Count the frequency of each value in input_arr and record it in its respective index in count_arr
    - 



Time Complexity: * N = input_arr size, M = count_arr size
    - Best Case: Omega( M + N )
    - Average Case: Theta( M + N )
    - Worst Case: O( M + N )
    
Comparison to Bucket Sort
    - Counting uses a bucket for every number from 0 to the max to hold their occurences
    - Bucket sort is a generalization of Counting sort
    - Counting sort becomes less practical when you have a large range of numbers
    - Counting only works with positive integers

Ultimately, the superior algorithm depends on the situation
    - Use counting sort for discrete integers with a limited range.
    - Use bucket sort when you have a broader range of values, especially with real numbers, and if the data is uniformly distributed.

'''
#_______________________________________________________________________________________

### Counting-sort algorithm function implementation
def counting_sort(input_arr = [7, 3, 5, 2, 5, 5, 2, 0, 4, 21, 1]):
    # Find the max value of the input array
    max_val = max(input_arr)

    # Initialize a "count array" that is of length (max_val + 1) and set all elements to 0
    # Each index should correspond to a possible number that can be in the array
    count_arr = [0 for i in range(max_val + 1)]

    # Count each occurance (frequency) of each number in input_arr and record it at its respective index in count_arr 
    for num_occurance in input_arr:
        count_arr[num_occurance] += 1

    # Calculate the cumulative sum of index i and index i - 1 for every elemet in count_arr (starting at index 1)
    for i in range(1, max_val + 1):
        count_arr[i] += count_arr[i - 1]

    # Initialize output_arr from count_arr
    output_arr = [0] * len(input_arr)

    for i in range(len(input_arr) - 1, -1, -1): # traverse array in reverse order to preserve order of equal elements
        output_arr[count_arr[input_arr[i]] - 1] = input_arr[i]
        count_arr[input_arr[i]] -= 1

    # Return the final sorted array
    return output_arr


#_______________________________________________________________________________________

### Main funtion
if __name__ == "__main__":
    print("\n*********************************")
    print("---  COUNTING-SORT ALGORITHM  ---")
    print("*********************************\n")

    # User gets the choice to view an example of counting-sort or try the algorithm with their own array
    # Take user input
    user_choice = int(input("Enter [1] to run example or [2] to try your own array: "))

    # [1] = Use provided array within counting-sort function
    if user_choice == 1:
        # display what the provided array is before sorting
        print("\n--> Example array: [7, 3, 5, 2, 5, 5, 2, 0, 4, 21, 1]")
        
        # print sorted array
        output_arr = counting_sort() # no arguement for example array
        print("Sorted array result =", output_arr)
        print("__________________________________________________________")

    # [2] = User would like to input their own array
    if user_choice == 2:
        # record user's array
        len = int(input("\nEnter array length: "))
        input_list = list(map(int, input("Enter array values (seperated by spaces): ").strip().split()))[:len]
    
        # print sorted array
        print("\n--> Inputted array:", input_list)
        output_arr = counting_sort(input_list) # arguement is the user-specified array
        print("Sorted array result =", output_arr)
        print("__________________________________________________________")
    
    # [  X  ] invalid number input
    if (user_choice != 1) and (user_choice != 2):
        print("\n[ X ] Invalid option, please rerun program and try again.")
        print("__________________________________________________________")
