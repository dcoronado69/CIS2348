# David Coronado People Soft ID:1971072 
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
# pivot, compare the values using two index variables l and h (low and high),
# initialized to the left and right sides of the current elements being sorted,
# and determine if a swap is necessary
def partition(user_ids, i, k):
    j = i - 1


# Take last element as pivot
pivot = user_ids[k]
# Loop will iterate through the user_ids
for x in range(i, k):
    # if any element is less than or equal pivot
    if (user_ids[x] <= pivot):
    # increment index of small element
        j = j + 1
# swapping small element with jth index element
user_ids[j], user_ids[x] = user_ids[x], user_ids[j]
user_ids[j + 1], user_ids[k] = user_ids[k], user_ids[j + 1]
return (i + 1)


# TODO: Write the quicksort algorithm that recursively sorts the low and
# high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):


# Take global element num_calls
    global num_calls
# it will increment it by 1 whenever this function calls
num_calls = num_calls + 1
if (i < k):
# calling partitioning funtion
    par = partition(user_ids, i, k)


