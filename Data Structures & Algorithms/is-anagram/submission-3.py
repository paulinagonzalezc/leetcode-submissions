class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hash Map / Frequency Counting.
        if len(s) != len(t):
            return False
        freq_s = {}
        freq_t = {}

        for i in range(len(s)):
            # increase count of i
            # is i in map already? No, then 1 + 0
            freq_s[s[i]] = 1 + freq_s.get(s[i], 0)
            freq_t[t[i]] = 1 + freq_t.get(t[i], 0)
        return freq_s == freq_t
