# Second Largest Element Finder

A Python solution to find the second largest unique element in an array.

## Problem Description

Given an array of integers `arr` of size `n`, the task is to identify and return the second largest unique value present in the array.

### Example
- **Input:** `arr = [8, 8, 4, 3, 6]`, `n = 5`
- **Output:** `6`
- **Explanation:** The unique elements in the array are `[8, 4, 3, 6]`. The maximum element is `8`, and the second largest unique element is `6`.

## Solution Approach

1. Convert the input array `arr` into a Python `set` to remove duplicate values.
2. Remove the maximum element from the set using `max()`.
3. Find and return the new maximum value from the remaining set elements.

## Time & Space Complexity

- **Time Complexity:** $\mathcal{O}(n)$ — Converting the list to a set and finding the maximum values both take linear time.
- **Space Complexity:** $\mathcal{O}(n)$ — Extra space is used to store the unique elements in a set.