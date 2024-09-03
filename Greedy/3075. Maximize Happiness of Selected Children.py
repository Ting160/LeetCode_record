You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

 

Example 1:

Input: happiness = [1,2,3], k = 2
Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.
Example 2:

Input: happiness = [1,1,1,1], k = 2
Output: 1
Explanation: We can pick 2 children in the following way:
- Pick any child with the happiness value == 1. The happiness value of the remaining children becomes [0,0,0].
- Pick the child with the happiness value == 0. The happiness value of the remaining child becomes [0,0].
The sum of the happiness values of the selected children is 1 + 0 = 1.
Example 3:

Input: happiness = [2,3,4,5], k = 1
Output: 5
Explanation: We can pick 1 child in the following way:
- Pick the child with the happiness value == 5. The happiness value of the remaining children becomes [1,2,3].
The sum of the happiness values of the selected children is 5.
 

Constraints:

1 <= n == happiness.length <= 2 * 105
1 <= happiness[i] <= 108
1 <= k <= n



# Sort + Greedy
# sort happiness from large to small
# for i in range(k)
#    res += max(happiness[i] - i, 0)
# Time: O(nlogn), Space: O(1)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        
        res = 0
        for i in range(k):
            res += max(happiness[i] - i, 0)
        
        return res


# Heapq
# Min heap
# Time: O(max(n, klogn)) = O(n), Space: O(k)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # O(n)
        heapq.heapify(happiness)
        # O(klogn)
        k_largest_list = heapq.nlargest(k, happiness)
        
        res = 0
        # O(k)
        for i in range(k):
            res += max(k_largest_list[i] - i, 0)
        
        return res



# Heapq
# Max heap
# Time: O(max(n, klogn)) = O(n), Space: O(1)
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # O(n)
        for i in range(len(happiness)):
            happiness[i] = -happiness[i]
        
        # O(n)
        heapq.heapify(happiness)
        
        # O(klogn)
        res = 0
        for i in range(k):
            res += max(-heapq.heappop(happiness) - i, 0)
        
        return res