import unittest
from src.exercises.dev_data_ops.ex4.ex4 import process_data, process_data_optimized

class TestEx4(unittest.TestCase):

    def test_ex4(self):
        self.assertEqual(True,True) #todo process_data(file_path), process_data_optimized(file_path))

if __name__ == '__main__':
    unittest.main()