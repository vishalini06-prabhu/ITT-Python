class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid_parentheses(n, open_count, curr, res):
            # If the current sequence has reached length 2 * n, add it to results
            if len(curr) == 2 * n:
                res.append(curr)
                return

            # Add opening parenthesis if we haven't used all n opening parentheses
            if open_count < n:
                valid_parentheses(n, open_count + 1, curr + '(', res)

            # Add closing parenthesis if the number of closing parentheses is less than the number of opening ones
            if len(curr) - open_count < open_count:
                valid_parentheses(n, open_count, curr + ')', res)

        result = []
        valid_parentheses(n, 0, '', result)
        return result
        
        
