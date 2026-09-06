# Check if an Array is Sorted

## Problem Description
Given an array of integers `arr` with size `n`, check whether the array is sorted in non-decreasing order or not. Return `true` if it is sorted in non-decreasing order; otherwise, return `false`.

## Approach
The current solution creates a new sorted version of the array using Python's built-in `sorted()` function and compares it directly with the original `arr`. If the original array matches the sorted array, it returns `True`, indicating the array is sorted in non-decreasing order; otherwise, it returns `False`.

## Complexity
- **Time Complexity:** O(N log N) - Sorting the array using `sorted()` takes O(N log N) time, where N is the number of elements in the array.
- **Space Complexity:** O(N) - Creating a sorted copy of the array requires O(N) additional space.