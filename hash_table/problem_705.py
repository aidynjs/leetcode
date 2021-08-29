import unittest

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash[key] = True     

    def remove(self, key: int) -> None:
        if key in self.hash:
            del self.hash[key]

    def contains(self, key: int) -> bool:
        return key in self.hash


class TestMyHashSet(unittest.TestCase):
    
    def setUp(self) -> None:
        self.my_hash_set = MyHashSet()

    def test_first_case(self):
        self.my_hash_set.add(1);      
        self.my_hash_set.add(2);      
        self.assertEqual(
            self.my_hash_set.contains(1),
            True
        )
        self.assertEqual(
            self.my_hash_set.contains(3),
            False
        )
        self.my_hash_set.add(2);      
        self.assertEqual(
            self.my_hash_set.contains(2),
            True
        )
        self.my_hash_set.remove(2)
        self.assertEqual(
            self.my_hash_set.contains(2),
            False
        )


if __name__ == "__main__":
    unittest.main()

