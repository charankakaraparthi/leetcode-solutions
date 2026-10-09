class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        balance = 0

        for ch in s:
            if ch == '(':
                # Each '(' requires two ')' -> balance increases by 2
                balance += 2
                
                # If we had an unmatched single ')' before this '(',
                # we must complete it with an inserted ')'
                if balance % 2 == 1:
                    insertions += 1
                    balance -= 1
            else:
                # Encountered a ')'
                balance -= 1
                
                # If balance becomes negative, we encountered a ')' without a preceding '('
                if balance < 0:
                    insertions += 1  # Insert an opening '('
                    balance += 2     # The inserted '(' adds 2 to balance (net result is 1)

        return insertions + balance