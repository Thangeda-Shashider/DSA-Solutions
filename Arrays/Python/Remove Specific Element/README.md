# Remove Specific Element

An in-place algorithm implemented in Python 3 to remove all occurrences of a target value from an array, shifting the remaining elements to the front and returning the new length.

## Problem Description

Given an array `arr` and an integer `target`, remove all occurrences of `target` in-place. The relative order of the non-target elements should be preserved, and they must be moved to the beginning of the array.

The function should return the length of the modified array containing non-target elements (`length`). The remaining elements beyond `length` do not matter.

### Example 1
```text
Input:
arr = [7, 8, 7, 6, 7, 5, 7]
target = 7

Output:
3
8 6 5