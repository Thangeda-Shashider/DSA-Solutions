class solution:
    def secondLargestElement(self, arr, n):
        unique_nums = set(arr)
        unique_nums.remove(max(unique_nums))
        new_max = max(unique_nums)
        return new_max