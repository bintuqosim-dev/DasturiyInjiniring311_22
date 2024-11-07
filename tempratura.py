def temp(tempratura):
    n = len(tempratura)
    list = [0] * n
    stack = []


    for i in range(n - 1, -1, -1):
        while stack and tempratura[i] >= tempratura[stack[-1]]:
            stack.pop()
        
        if stack:
            list[i] = stack[-1] - i
        
        stack.append(i)
    
    return list
tempratura = [73, 74, 75, 71, 69, 72, 76, 73]
# tempratura = [10,5,6]
print(temp(tempratura))
