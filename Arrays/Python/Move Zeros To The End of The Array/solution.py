class solution:
    def moveZerosToEnd(self, arr, n):
        i = 0
        for j in range(n):
            if arr[j] != 0:
                arr[i] = arr[j]
                i += 1 
        while i < n:
            arr[i] = 0
            i += 1 
        return arr