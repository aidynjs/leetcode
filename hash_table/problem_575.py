import unittest
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        unique_candy_type = set(candyType)
        return n if n < len(unique_candy_type) else len(unique_candy_type)

        


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        self.assertEqual(
            self.solution.distributeCandies([1,1,2,2,3,3]),
            3
        )

    def test_second_case(self):
        self.assertEqual(
            self.solution.distributeCandies([1,1,2,3]),
            2
        )

    def test_third_case(self):
        self.assertEqual(
            self.solution.distributeCandies([6,6,6,6]),
            1
        )


if __name__ == "__main__":
    unittest.main()