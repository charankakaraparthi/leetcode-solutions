from collections import deque

class Solution:
    def removeInvalidParentheses(self, s):
        def is_valid(string):
            count = 0

            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            # If a valid string is found at this level,
            # don't generate strings with more removals.
            if found:
                continue

            for i in range(len(current)):
                # Only remove parentheses
                if current[i] not in "()":
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result