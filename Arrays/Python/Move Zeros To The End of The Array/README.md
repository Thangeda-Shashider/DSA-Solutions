# Move Zeros to the End of an Array

A Python 3 solution to shift all zeros in an array to the end while maintaining the original relative order of all non-zero elements in-place.

---

## Problem Description

Given an array of integers `arr` of size `n`, move all the zeros present in the array to the end. The relative order of the non-zero elements must remain unchanged.

### Examples

**Example 1:**
- **Input:** `n = 7`, `arr = [0, 1, 0, 3, 0, 12, 0]`
- **Output:** `[1, 3, 12, 0, 0, 0, 0]`

**Example 2:**
- **Input:** `n = 5`, `arr = [0, 0, 0, 0, 0]`
- **Output:** `[0, 0, 0, 0, 0]`

---

## Constraints

* $1 \le n \le 10^4$
* $-10^6 \le arr[i] \le 10^6$

---

## Approach & Algorithm

The problem is solved using a **Two-Pointer Strategy** to modify the array in-place with $O(1)$ auxiliary space complexity:

1. **Shift Non-Zero Elements:** 
   Maintain an index pointer `i` starting at `0` for writing non-zero elements. Iterate through the array using a read pointer `j` from `0` to `n - 1`. Whenever `arr[j]` is non-zero, assign `arr[i] = arr[j]` and increment `i`.
2. **Fill Remaining Positions with Zeros:** 
   Once all non-zero elements are placed, run a second loop starting from index `i` up to `n - 1` and set each element to `0`.

---