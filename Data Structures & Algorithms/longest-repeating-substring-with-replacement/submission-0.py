class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        freq = {}

        left = 0
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] += 1
            else:
                freq[s[i]] = 1

            max_freq = max(freq.values()) 
            length_window = i - left + 1

            while length_window - max_freq > k:
                freq[s[left]] -= 1
                left += 1 #moving the window one over
                length_window = i - left + 1
                max_freq = max(freq.values())

            if length_window > max_length:
                max_length = length_window

        return max_length