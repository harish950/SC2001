def hybrid_mergesort(arr, counter, threshold=10):
    """
    Hybrid sorting algorithm combining Merge Sort and Insertion Sort
    
    Args:
        arr: List of comparable elements to sort
        threshold: Size threshold below which to use insertion sort (default: 10)
        counter: number of comparisons
    Returns:
        Sorted array
    """
    if not arr:
        return arr
    
    # Create a copy to avoid modifying the original array
    arr_copy = arr.copy()
    _hybrid_mergesort_helper(arr_copy, 0, len(arr_copy) - 1, threshold, counter)
    return arr_copy


def _hybrid_mergesort_helper(arr, left, right, threshold, counter):
    """
    Recursive helper function for hybrid mergesort
    
    Args:
        arr: Array to sort (modified in-place)
        left: Starting index of subarray
        right: Ending index of subarray
        threshold: Size threshold for switching to insertion sort
        counter: number of comparisons
    """
    if left < right:
        size = right - left + 1
        
        # If subarray size is small, use insertion sort
        if size <= threshold:
            _insertion_sort(arr, left, right, counter)
        else:
            # Otherwise, use mergesort
            mid = left + (right - left) // 2
            _hybrid_mergesort_helper(arr, left, mid, threshold, counter)
            _hybrid_mergesort_helper(arr, mid + 1, right, threshold, counter)
            _merge_sort(arr, left, mid, right, counter)


def _insertion_sort(arr, left, right, counter):
    """
    Insertion sort for a specific range of the array.
    
    Args:
        arr: Array to sort (modified in-place)
        left: Starting index
        right: Ending index (inclusive)
    """
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j>=left:
            counter[0]+=1
            if arr[j]>key:
                arr[j+1]=key
                j-=1
            else:
                break
        arr[j + 1] = key


def _merge_sort(arr, left, mid, right, counter):
    """
    Merge two sorted subarrays arr[left:mid+1] and arr[mid+1:right+1].
    
    Args:
        arr: Array containing the subarrays (modified in-place)
        left: Starting index of first subarray
        mid: Ending index of first subarray
        right: Ending index of second subarray
    """
    # Create temporary arrays for the two subarrays
    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]
    
    # Merge the temporary arrays back into arr[left:right+1]
    i = j = 0  # Initial indexes for left_arr and right_arr
    k = left   # Initial index for merged array
    
    while i < len(left_arr) and j < len(right_arr):
        counter[0]+=1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    # Copy remaining elements of left_arr, if any
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    # Copy remaining elements of right_arr, if any
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


# chatgpt Example usage and testing
if __name__ == "__main__":
    import random
    import time
    
    def test_correctness():
        """Test the correctness of the hybrid algorithm."""
        test_cases = [
            [],
            [1],
            [3, 2, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 7, 1, 9, 4, 6, 2, 8, 5],
            [1, 3, 2, 4, 6, 5, 8, 7, 10, 9],
        ]
        counter = [0]
        for i, arr in enumerate(test_cases):
            original = arr.copy()
            sorted_arr = hybrid_mergesort(arr, counter)
            expected = sorted(original)
            
            print(f"Test {i+1}: {original}")
            print(f"Result:  {sorted_arr}")
            print(f"Correct: {sorted_arr == expected}")
            print()
    
    def performance_comparison():
        """Compare performance with different thresholds."""
        size = 10000
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        thresholds = [1, 5, 10, 20, 50]
        
        print(f"Performance comparison on array of size {size}:")
        print("Threshold | Time (seconds)")
        print("-" * 25)
        
        for threshold in thresholds:
            arr_copy = arr.copy()
            start_time = time.time()
            hybrid_mergesort(arr_copy, threshold)
            end_time = time.time()
            
            print(f"{threshold:8d} | {end_time - start_time:.6f}")
    
    # Run tests
    print("=== Correctness Tests ===")
    test_correctness()
    
    print("=== Performance Comparison ===")
    performance_comparison()