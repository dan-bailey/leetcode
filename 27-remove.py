def removeElement(nums, val):
    targets = 0
    out = []
    for x in range(0, len(nums)):
        if nums[x] != val:
            targets += 1
            out.append(nums[x])
    print(out)

removeElement([3, 2, 2, 3], 3)