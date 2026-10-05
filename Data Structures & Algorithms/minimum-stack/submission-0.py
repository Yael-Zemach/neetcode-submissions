class MinStack:

    def __init__(self):
        self._stack = []
        self._min = 2**31-1

    def push(self, val: int) -> None:
        obj = {"value": val}
        if not self._stack:
            obj["min_value"] = val
        else:
            obj["min_value"] = min(val, self._stack[-1]["min_value"])
        self._stack.append(obj)

    def pop(self) -> None:
        self._stack.pop()
        

    def top(self) -> int:
        return self._stack[-1]["value"]

    def getMin(self) -> int:
        return self._stack[-1]["min_value"]

        
