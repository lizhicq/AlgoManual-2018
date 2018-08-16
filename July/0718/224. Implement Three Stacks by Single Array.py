class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.array = [None for _ in range(3*size)]
        self.indexs ={0:0, 1:size, 2:2*size}

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        if self.indexs[stackNum] < (stackNum+1) * self.size:
            self.array[self.indexs[stackNum]] = value
            self.indexs[stackNum] += 1

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        self.indexs[stackNum] -= 1
        return self.array[self.indexs[stackNum]]
    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        index  = self.indexs[stackNum]
        return self.array[index-1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        return self.indexs[stackNum] == stackNum * self.size


if __name__ == "__main__":
    s = ThreeStacks(5)
    s.push(0, 10)
    s.push(0, 11)
    s.push(1, 20)
    s.push(1, 21)
    s.pop(0)
    s.pop(1)
    s.peek(1)
    s.push(2, 30)
    s.pop(2)
    s.isEmpty(2)
    s.isEmpty(0)