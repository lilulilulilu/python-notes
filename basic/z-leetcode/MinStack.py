class MinStack:

    def __init__(self):
        self.mins = [] # 用存储来栈arr每个元素对应的最小值
        self.arr = []
        self.length = 0

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.length = self.length + 1
        
        if self.length == 1:
            self.mins.append(val)
        else:
            last_min = self.mins[self.length-2]
            if val < last_min:
                self.mins.append(val)
            else:
                self.mins.append(last_min)         

    def pop(self) -> None:
        if self.length > 0:
            self.arr.pop()
            self.mins.pop()
            self.length = self.length - 1

    def top(self) -> int:
        if self.length > 0:
            return self.arr[self.length-1]
        else:
            return None

    def getMin(self) -> int:
        if self.length > 0:
            top_index = self.length - 1
            return self.mins[top_index]
        else:
            return None
        



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(3)
obj.push(1)
obj.push(4)

obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)