class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        chkd = []

        for num in nums:
            if num in chkd:
                return True
            else:
                chkd.append(num)
        return False