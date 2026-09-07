class solution:
    def secondSmallestElement(self, arr, n):
        unique_elements = set(arr)
        unique_elements.remove(min(unique_elements))
        result = min(unique_elements)
        return result
        