import unittest
from src.example_model import create_model

class TestModel(unittest.TestCase):

    def test_model_creation(self):
        model = create_model()
        self.assertEqual(len(model.layers), 5)
        self.assertEqual(model.input_shape, (None, 64, 64, 3))

if __name__ == '__main__':
    unittest.main()