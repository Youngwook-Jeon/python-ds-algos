class FenwickTree:
    def __init__(self, nums):
        # original array of int numbers
        self.nums = nums
        # the constructed Fenwick tree
        self.fenwick_tree = [0 for _ in range(len(nums) + 1)]
    
    # O(NlogN) running time complexity
    def construct(self):
        # consider all the items in the original array
        for index in range(1, len(self.nums) + 1):
            self.update(index, self.nums[index - 1])
    
    # the sum of numbers in the interval [start:end]
    # O(logN) running time complexity
    def range_sum(self, start, end):
        return self.sum(end) - self.sum(start - 1)
    
    # sum of the integers in the range [0:index] PREFIX SUM
    # O(logN) running time complexity
    def sum(self, index):
        index = index + 1
        sum = 0
        while index > 0:
            # binary index tree contains the sums of given ranges
            sum = sum + self.fenwick_tree[index]
            # go to the parent and keep going (basically the items on the left)
            index = self.parent(index)
        
        return sum
    
    # update an existing item in the tree with index and value accordingly
    # O(logN) running time complexity
    def update(self, index, num):
        # have to check all the ranges that include the index
        while index < len(self.nums) + 1:
            self.fenwick_tree[index] += num
            # index of the next items
            index = self.next(index)
    
    # index of the item on the left
    # O(1) running time complexity
    def next(self, index):
        return index + (index & -index)

    def parent(self, index):
        return index - (index & -index)

if __name__ == "__main__":
    nums = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    tree = FenwickTree(nums)
    tree.construct()
    print(tree.range_sum(2, 5)) # 14