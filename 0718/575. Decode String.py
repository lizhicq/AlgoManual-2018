class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def stack_pop(self, stack):
        tmp = ""
        while stack:
            if stack[-1].isdigit():
                break
            tmp = stack.pop() + tmp
        return tmp

    def expressionExpand(self, s):
        stack = []
        num = 0
        res = ''
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch is '[':
                stack.append(str(num))
                num = 0
            elif ch is ']':
                tmp = self.stack_pop(stack)
                times = int(stack.pop())
                string = times * tmp
                stack.append(string)
            else:
                stack.append(ch)
        return ''.join(stack)




if __name__ == "__main__":
    s = Solution()
    print s.expressionExpand('3[2[ad]3[pf]]xyz')