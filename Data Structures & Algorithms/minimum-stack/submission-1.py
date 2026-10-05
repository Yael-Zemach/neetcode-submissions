class MinStack:

    def __init__(self):
        self._stack = []

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

        
