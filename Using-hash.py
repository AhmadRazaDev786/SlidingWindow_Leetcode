class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        longest = 0
        left = 0  
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            longest = max(longest, right - left + 1)

        return longest