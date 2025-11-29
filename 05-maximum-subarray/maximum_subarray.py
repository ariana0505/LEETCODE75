nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSub = nums[0]
sumaActual = 0
for i in nums:
    if nums[i] < 0:
        sumaActual = 0
    sumaActual += i 
    maxSub = max(maxSub, sumaActual)