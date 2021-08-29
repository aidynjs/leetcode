import unittest

from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if num in arr:
                return num
            else:
                arr.append(num)



class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        self.assertEqual(
            self.solution.repeatedNTimes([1,2,3,3]),
            3
        )

    def test_second_case(self):
        self.assertEqual(
            self.solution.repeatedNTimes([2,1,2,5,3,2]),
            2
        )

    def test_third_case(self):
        self.assertEqual(
            self.solution.repeatedNTimes([5,1,5,2,5,3,5,4]),
            5
        )


if __name__ == "__main__":
    unittest.main()