class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        s1 = []
        for i in range(len(s)):
            if stack and s[i] == "#":
                stack.pop()
            elif not stack and s[i] == "#":
                continue
            else:
                stack.append(s[i])
        for j in range(len(t)):
            if s1 and t[j] == "#":
                s1.pop()
            elif not s1 and t[j] == "#":
                continue
            else:
                s1.append(t[j])
        return stack == s1

        