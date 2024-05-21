def solution(nums):
    ret=[]
    for i in range(len(nums)):
        maxium=nums[i:][0]
        result=[]
        for j in nums[i:]:
            if j>=maxium:
                maxium =j
                result.append(j)
                if len(result)>len(ret):
                    ret=result
        return ret
print(solution([0,1,1,2,2,3,2,6,6,4]))

