def findPosition(nums, target):
    for x in range(len(nums)):
        if nums[x] >= target:
            return x
    return len(nums) # if there's no target, it gets stuck at the end of the list

print(findPosition([1,3,5,6], 5)) # 2
print(findPosition([1,3,5,6], 2)) # 1
print(findPosition([1,3,5,6], 7)) # 4