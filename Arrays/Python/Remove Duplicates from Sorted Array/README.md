# Remove Duplicates from Sorted Array

## Problem Description
Given a sorted integer array `arr` of size `n`, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `arr`.

## Approach
I used a two-pointer approach to solve this problem optimally in a single pass:
1. Initialize a pointer `i` at index 0 to keep track of the position of the last unique element found.
2. Use a loop with pointer `j` starting from index 1 to scan through the array.
3. Whenever `arr[j]` is different from `arr[i]`, it means a new unique element has been found.
4. Increment `i` by 1 and update `arr[i]` with the value at `arr[j]`.
5. Return `i + 1`, which represents the total count of unique elements.

## Complexity
- **Time Complexity:** $O(N)$ - We iterate through the array exactly once using the pointer `j`, where $N$ is the number of elements in the array.
- **Space Complexity:** $O(1)$ - The array is modified in-place, requiring no extra space.