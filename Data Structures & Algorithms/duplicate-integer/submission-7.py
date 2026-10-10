class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Pattern: Hash Set / Seen Elements pattern
        # nums = [1, 2, 3, 4]

        values = set()

        for num in nums:
            if num in values:
                return True
            else:
                values.add(num)
        
        return False

        
        # return True
        # return False
