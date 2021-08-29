import unittest

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        histogram = {}
        for char in s:
            if char in histogram.keys():
                histogram[char] += 1
            else:
                histogram[char] = 1
        values = list(histogram.values())
        return len(set(values)) <= 1


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_first_case(self):
        self.assertEqual(
            self.solution.areOccurrencesEqual("abacbc"),
            True
        )

    
    def test_second_case(self):
        self.assertEqual(
            self.solution.areOccurrencesEqual("aaabb"),
            False
        )

    def test_third_case(self):
        self.assertEqual(
            self.solution.areOccurrencesEqual("tveixwaeoezcf"),
            False
        )


    def test_fourth_case(self):
        self.assertEqual(
            self.solution.areOccurrencesEqual("fhojjkontbncdhwxbnexplclvjyexzsvqyyhpfpnvhdskuhkuoihiqgalklqketjikdlgrawhfo"),
            False
        )


if __name__ == '__main__':
    unittest.main()