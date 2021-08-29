import unittest

class MyHashMap:

    def __init__(self):
        self.map = {}
   

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.map:
            del self.map[key]


class TestMyHashMap(unittest.TestCase):

    def setUp(self) -> None:
        self.my_hash_map = MyHashMap()

    def test_first_case(self):
        self.my_hash_map.put(1, 1); 
        self.my_hash_map.put(2, 2); 
        self.assertEqual(
            self.my_hash_map.get(1),
            1
        )
        self.assertEqual(
            self.my_hash_map.get(3),
            -1
        )
        self.my_hash_map.put(2, 1); 
        self.assertEqual(
            self.my_hash_map.get(2),
            1
        )
        self.my_hash_map.remove(2); 
        self.assertEqual(
            self.my_hash_map.get(2),
            -1
        )


if __name__ == "__main__":
    unittest.main()