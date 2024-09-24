class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seti = set()
        longest = 0
        left = 0  
        for right in range(len(s)):
            while s[right] in seti:
                seti.remove(s[left])
                left += 1
            seti.add(s[right])
            longest = max(longest, right - left + 1)

        return longest