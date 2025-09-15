def max_sum_subarray_fixed_k(arr, k):
    n = len(arr)
    if n < k:
        return -1  # Or raise an error

    current_sum = sum(arr[:k])  # Calculate sum of the first window
    max_sum = current_sum

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(f"Maximum sum of subarray of size {k}: {max_sum_subarray_fixed_k(arr, k)}")

def longest_subarray(nums, k):
    left = 0
    curr_sum = 0
    max_length = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage
nums = [1, 2, 3, 4, 5]
k = 7
print(longest_subarray(nums, k))  # Output: 3