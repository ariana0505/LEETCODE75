nums = [-1,0,1,2,-1,-4]
nums.sort()
answer = []
for i , v in enumerate(nums):
    if i> 0 and nums[i] == nums[i-1]:
        continue
    l , r = i +1 , len(nums) - 1
    while l < r :
        sum3 = v + nums[l] + nums[r]
        if 0 > sum3:
            l += 1
        elif 0 < sum3:
            r -= 1
        else:
            answer.append([v , nums[l] , nums[r]])
            l += 1
            r -= 1

            while l < r and nums[l] == nums[l - 1]:
                l += 1

            while l < r and nums[r] == nums[r + 1]:
                r -= 1

print(answer)