class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == "{":
                stack.append(symbol)
            elif symbol == "(":
                stack.append(symbol)
            elif symbol == "[":
                stack.append(symbol)
            elif len(stack) == 0:
                return False
            elif symbol == "}":
                if len(stack) > 0 and stack.pop() != "{":
                    return False
            elif symbol == ")":
                if len(stack) > 0 and stack.pop() != "(":
                    return False
            elif symbol == "]":
                if len(stack) > 0 and stack.pop() != "[":
                    return False

        if len(stack) != 0:
            return False

        return True