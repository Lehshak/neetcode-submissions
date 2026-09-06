class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = dict()
        suffix = dict()

        p = 0
        for i in range(len(height)):
            p = max(p, height[i])
            prefix[i] = p

        s = 0
        for i in range(len(height)-1, -1, -1):
            s = max(s, height[i])
            suffix[i] = s
        

        water = 0
        # first and last can never hold any water
        for i in range(1, len(height)-1):
            min_bar = min(prefix[i-1], suffix[i+1])

            water += max(0, min_bar - height[i])

        return water

        