# Majority Element

## Problem Description

Given an array `arr` of size `n`, the task is to find and return the **majority element**.

The majority element is defined as the element that appears more than $\lfloor n / 2 \rfloor$ times in the array. You may assume that the majority element always exists in the array.

### Examples

**Example 1:**
- **Input:** `n = 5`, `arr = [2, 2, 1, 2, 3]`
- **Output:** `2`
- **Explanation:** $\lfloor 5 / 2 \rfloor = 2$. The element `2` appears 3 times, which is strictly greater than 2.

**Example 2:**
- **Input:** `n = 10`, `arr = [5, 5, 2, 5, 4, 7, 4, 5, 5, 5]`
- **Output:** `5`
- **Explanation:** $\lfloor 10 / 2 \rfloor = 5$. The element `5` appears 6 times, which is strictly greater than 5.

---

## Constraints

* $1 \le n \le 5000$
* $-10^7 \le \text{arr}[i] \le 10^7$
