height = [7,9,3,1,7,15,10,4,5]
l,r= 0 , len(height)-1
area_maxima = 0
while l<r :
    area = min(height[l], height[r]) * (r-l)
    area_maxima = max(area_maxima,area)
    if height[l]> height[r]:
        r-=1
    else:
        l+= 1

print(area_maxima)