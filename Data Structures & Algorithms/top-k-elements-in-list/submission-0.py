class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq_rev = dict()

        for key, value in freq.items():
            if value in freq_rev:
                freq_rev[value].append(key)
            else:
                freq_rev[value] = [key]

        most_frequent_keys = list(freq_rev.keys())
        most_frequent_keys.sort(reverse=True)

        group_freqs = []

        for key in most_frequent_keys:
            group_freqs.extend(freq_rev[key])

        return group_freqs[:k]

        



            



        