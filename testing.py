import unittest
import QuantityUnitExtraction


class MyTestCase(unittest.TestCase):
    def test_extract_quantity(self):
        self.assertEqual(
            QuantityUnitExtraction.extract_quantity_unit("1 teaspoon baking powder"),
            (1, "teaspoon")
        )
        self.assertEqual(
            QuantityUnitExtraction.extract_quantity_unit("1/2 teaspoon baking powder"),
            (0.5, "teaspoon")
        )
        self.assertEqual(
            QuantityUnitExtraction.extract_quantity_unit("1 head cabbage, cored and coarsely chopped"),
            (1, "head cabbage")
        )


if __name__ == '__main__':
    unittest.main()
