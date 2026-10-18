class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []         
        best = 0
        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx
            stack.append((start, h))

        for idx, height in stack:
            best = max(best, height * (n - idx))

        return best