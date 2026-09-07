class solution:
    def majorityElement(self, arr):
        num = len(arr) // 2
        for i in arr:
            if arr.count(i) > num:
                return i