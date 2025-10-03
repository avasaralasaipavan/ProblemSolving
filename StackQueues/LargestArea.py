def largestRectangleArea(heights):
    stack = []  
    max_area = 0
    heights.append(0)  

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            height = heights[top]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area

heights = [1,1,1,1]
print(largestRectangleArea(heights))