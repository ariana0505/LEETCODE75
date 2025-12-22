height = [1,1]
Output: 1
maximum_area = 0
l, r = 0 , len(height)-1
while l < r:
    area_actual = min(height[l], height[r]) * ( r - l)
    maximum_area = max(area_actual,maximum_area)
    if l< r:
        l =l + 1
    else:
        r = r -1
print(maximum_area)