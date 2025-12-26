nums = [4,5,6,7,0,1,2]
target = 9
l = 0
r = len(nums) - 1
while l <= r:
    m = (l + r) //2
    if nums[m] == target:
        print(m)
        break
    if nums[l] < nums[m]:
        if nums[l] <= target < nums[m]:
            r = m - 1
        else:
            l = m + 1 
    else:
        if nums[m] < target <= nums[r]:
            l = m + 1
        else:
            r = m - 1
else:
    print(-1)