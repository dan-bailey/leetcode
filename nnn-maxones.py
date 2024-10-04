class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSteps = 0
        highest = 0
        for num in nums:
            if num == 1:
                maxSteps +=1
                if maxSteps > highest:
                    highest = maxSteps
            elif num == 0:    
                maxSteps = 0
        return highest