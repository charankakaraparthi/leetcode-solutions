class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"

        count = 0

        # First window
        for i in range(k):
            if s[i] in vowels:
                count += 1

        ans = count

        # Slide the window
        for i in range(k, len(s)):
            # Add new character
            if s[i] in vowels:
                count += 1

            # Remove old character
            if s[i - k] in vowels:
                count -= 1

            ans = max(ans, count)

        return ans