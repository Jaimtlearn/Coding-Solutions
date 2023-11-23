class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # ans = []
        # for i in range(len(l)):
        #     print(f'r and l {r[i]} && {l[i]}')
        #     if r[i] - l[i] + 1 <=  2:
        #         ans.append(True)
        #         continue
        #     temp = nums[l[i]:r[i]+1]
        #     temp.sort()
        #     print(temp)
        #     f = True
        #     d = temp[1] - temp[0]
        #     for j in range(1,len(temp)-1):
        #         if temp[j+1] - temp[j] != d:
        #             f = False
        #             break
        #     ans.append(f)
        # return ans
        ans = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            x = [temp[j+1]-temp[j] for j in range(len(temp)-1)]
            if len(set(x)) == 1:
                ans.append(True)
            else:
                ans.append(False)
        return ans