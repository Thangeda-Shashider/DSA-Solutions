class solution:
    def pascalsTriangle(self, n):
        if n == 1:
            return [[1]]
        if n == 2:
            return [[1], [1, 1]]
        ans = [[1], [1, 1]]
        prev = [1, 1]
        for i in range(3, n + 1):
            cur = [1] * i
            for j in range(1, i - 1):
                cur[j] = prev[j] + prev[j - 1]
            ans.append(cur)
            prev = cur
        return ans