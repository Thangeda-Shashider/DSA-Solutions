class solution:
    def removeSpecificElement(self, arr, target):
        i = 0
        for j in range(len(arr)):
            if arr[j] != target:
                arr[i] = arr[j]
                i += 1 
        return i        