class ProductOfNumbers:

    def __init__(self):
        self.stack=[]
        

    def add(self, num: int) -> None:
        self.stack.append(num)

    def getProduct(self, k: int) -> int:
        return prod(self.stack[-k:])

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
