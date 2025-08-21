def trap(height):
    n = len(height)
    if n < 3:  # Fewer than 3 bars -> no water
        return 0

    left, right = 0, n - 1
    leftMax, rightMax = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1

    return water
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  
print(trap([4,2,0,3,2,5]))              
print(trap([1,1,1]))                    
print(trap([5]))                        
print(trap([2,0,2]))                    
print(trap([0,0,0,0]))                 
print(trap([1,2,3,4,5]))               
print(trap([5,4,3,2,1]))                
