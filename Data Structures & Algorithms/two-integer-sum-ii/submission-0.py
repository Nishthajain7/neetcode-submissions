class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head=0
        tail=len(numbers)-1
        while head<tail:
            total=numbers[head]+numbers[tail]
            if total==target:
                return [head+1, tail+1]
            elif total<target:
                head+=1
            else:
                tail-=1
