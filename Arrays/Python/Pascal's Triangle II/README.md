# Pascal's Triangle II

An efficient implementation to compute the $k^{\text{th}}$ row of Pascal's Triangle (0-indexed).

## Problem Description

Given an integer `k`, return the $k^{\text{th}}$ (0-indexed) row of Pascal's triangle.

### Rules of Pascal's Triangle
- The first and last elements of each row are always `1`.
- Every internal element is equal to the sum of the two elements directly above it in the previous row.

---

## Examples

### Example 1
```text
Input: k = 4
Output: [1, 4, 6, 4, 1]