class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        chkd = set()

        for num in nums:
            if num in chkd:
                return True
            else:
                chkd.add(num)
        return False