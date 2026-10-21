class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total>0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    if  [nums[i], nums[l], nums[r]] not in out:
                        out.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
        return out

        

            
        