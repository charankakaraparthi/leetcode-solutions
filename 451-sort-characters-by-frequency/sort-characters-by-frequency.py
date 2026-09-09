class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        # Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Sort by frequency in decreasing order
        chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Build result
        ans = ""

        for ch, count in chars:
            ans += ch * count

        return ans