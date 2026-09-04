# Duplicate Zeros

## Problem Description
Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right. Modify the input array **in-place** without returning anything.

## Approach
I used a `while` loop to iterate through the array. When a `0` is encountered, I use Python's `.insert()` method to add a new `0` exactly one position ahead (`i + 1`). To maintain the fixed length of the array, I use `.pop()` to remove the last element. Finally, I increment the index by 2 to skip the newly added zero and prevent an infinite loop.

## Complexity
- **Time Complexity:** O(N^2) - Iterating through the array takes O(N), and the `.insert()` method takes O(N) in the worst case, leading to O(N^2).
- **Space Complexity:** O(1) - The array is modified in-place, requiring no extra space.