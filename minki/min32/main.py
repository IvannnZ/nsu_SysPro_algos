class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump_in_time = 0

        for i in nums:
            if max_jump_in_time == -1:
                return False
            max_jump_in_time = max(max_jump_in_time, i)
            max_jump_in_time -= 1
            
        
        return True
