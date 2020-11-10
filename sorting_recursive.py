def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(n(log n)) WorstCase BestCase AverageCase, Actual sorting of each half, and combining them is O(n) n being the smaller array
    Memory usage: O(n logn) Each merge, returns a new list and theres log n merges."""
    # Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items
    # Split items list into approximately equal halves
    mid = len(items) // 2 # Sets the midpoint of the array
    # Sort each half by recursively calling merge sort
    l = items[:mid] # Takes left half of array
    r = items[mid:] # Takes right half of array
    left = merge_sort(l) # Recursivly runs mergesort on left
    right = merge_sort(r) # Recursivly runs mergesort on right
    result = [] # Init result arr
    # Merge sorted halves into one list in sorted order
    while len(left) > 0 and len(right) > 0: # Run until either left or right is empty
        if left[0] < right[0]: # Checks if left element is less than right
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    # At this point result has half the sorted array, and left or right has the other half
    for i in left: # Add left to result
        result.append(i) 
    for i in right: # Add right to result
        result.append(i)
    return result

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best/Average case running time: O(nlogn) 
    Worst case running time: O(n^2) If the list is already sorted, I set pivot to high, and force every element below it, and it continues until every element has become a pivot, not counting index 0
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Check if high and low range bounds have default values (not given)
    if low == None:
        low = 0
    if high == None:
        high = len(items) - 1
    # Check if list or range is so small it's already sorted (base case)
    if low < high: # If low is = then the array is size 1
        # Partition items in-place around a pivot and get index of pivot
        pivot = partition(items, low, high)# Define pivot
        # Sort each sublist range by recursively calling quick sort
        # Now Run quick sort on both of the two partitioned arrays
        quick_sort(items, low, pivot - 1) # Everything to the left of the pivot
        quick_sort(items, pivot + 1, high) # Everything to the right of the pivot
    else:
        return items # If list is size 1 or its finished with partitioning

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) n being the number of elements in the partitioned array.
    Memory usage: O(1) Pretty sure no new memory is created, because after function is over, temp variables are deleted because they become out of scope."""
    index = low - 1
    # Choose a pivot any way and document your method in docstring above
    pivot = items[high] # Pivot will always be high pointer
    # Loop through the partioned array using the low and high boundaries.
    for j in range(low , high): 
        # If current element is smaller or equal to the pivot 
        if items[j] <= pivot: 
            # Move items less than pivot into front of range
            index += 1 
            items[index], items[j] = items[j], items[index] 
    # Move items greater than pivot into back of range 
    items[index + 1], items[high] = items[high], items[index + 1]
    return index + 1