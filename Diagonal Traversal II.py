"""
1. Diagonal elements which are to be together, there sum of indexes are same
eg: 1,0 and 0,1 there sum is 1. 2,0 1,1 1,2 are in diagonal and have same sum
2. Inserting them accoring to there sum
3. reversing them after traversal is done
"""

from itertools import chain
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i,n in enumerate(nums):
            for j,x in enumerate(n):
                while i+j>=len(ans):
                    ans.append([])
                ans[i+j].append(x)
        print(ans)
        ans = [reversed(x) for x in ans]
        return list(chain(*ans))