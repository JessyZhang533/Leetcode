class RandomizedSet_1:

    def __init__(self):
        self.set = {}

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set[val] = True
            return self.set[val]
        return False

    def remove(self, val: int) -> bool:
        if val in self.set:
            del self.set[val]  # !!!
            return True
        return False

    def getRandom_1(self) -> int:
        import random  # !!!
        return random.choice(list(self.set.keys()))  # !!! 1. random.choice(), not ideal O(logn); 2. how to get a list of keys of a dic

    def getRandom_2(self):
        import random
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()