import unittest
from pest import Pest

class TestPest(unittest.TestCase):
    def setUp(self):
        return super().setUp()
 
    def tearDown(self):
        return super().tearDown()
 
    def test_pest_initialization(self):
        p = Pest("Aphid", "FruitTree", 10)
        self.assertEqual(p.name, "Aphid")
        self.assertEqual(p.affected_plant, "fruittree")
        self.assertEqual(p.week_detected, 10)

    def test_invalid_affected_plant(self):
        with self.assertRaises(ValueError):
            Pest("Aphid", "Flower", 10)

    def test_invalid_week_detected(self):
        with self.assertRaises(ValueError):
            Pest("Aphid", "Vegetable", 0)
        with self.assertRaises(ValueError):
            Pest("Aphid", "Vegetable", 53)