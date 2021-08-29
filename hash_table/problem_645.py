import unittest
from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic={}
        missing = None
        for i in nums:
            if i in dic:
                missing = i
                break
            else:
                dic[i]=1
        summ=sum(nums)
        ans = len(nums)*(len(nums)+1)//2 - summ
        return [missing, missing+ans]



class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        self.assertEqual(
            self.solution.findErrorNums([1,2,2,4]),
            [2,3]
        )

    def test_second_case(self):
        self.assertEqual(
            self.solution.findErrorNums([1,1]),
            [1,2]
        )

    def test_third_case(self):
        self.assertEqual(
            self.solution.findErrorNums([2,2]),
            [2,1]
        )

    def test_fourth_case(self):
        self.assertEqual(
            self.solution.findErrorNums([1,3,3]),
            [3, 2]
        )

if __name__ == "__main__":
    unittest.main()