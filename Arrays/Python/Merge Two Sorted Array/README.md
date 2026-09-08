# Merge Two Sorted Arrays

A Python 3 solution for merging two sorted integer arrays `arr1` and `arr2` in non-decreasing order directly in-place.

## 📝 Problem Statement

You are given two integer arrays `arr1` and `arr2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `arr1` and `arr2`, respectively.

The task is to merge `arr2` into `arr1` as a single sorted array in non-decreasing order.

### Constraints & Conditions
- The final sorted array must be stored inside `arr1` directly (in-place modification).
- `arr1` has a length of `m + n`. The first `m` elements are the initial valid elements, and the last `n` elements are initialized to `0` as placeholders.
- `arr2` has a length of `n`.
- $0 \le m, n \le 500$
- $1 \le m + n \le 500$
- $-10^9 \le \text{arr1}[i], \text{arr2}[i] \le 10^9$

---

## 💡 Example

**Input:**
```text
m = 4, n = 3
arr1 = [1, 3, 5, 7, 0, 0, 0]
arr2 = [2, 4, 6]