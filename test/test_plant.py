import unittest
from plant import Plant
from plant import FruitTree
from plant import Vegetable

class TestPlant(unittest.TestCase):
    def setUp(self):
        return super().setUp()
 
    def tearDown(self):
        return super().tearDown()
 
    def test_add_harvest_week(self):
        p = Plant("Tomato")
        p.add_harvest_week(12)
        self.assertIn(12, p.harvest_weeks)

    def test_add_yield_for_week(self):
        p = Plant("Carrot")
        p.add_yield_for_week(15, 2.5)
        self.assertEqual(p.yields_per_week[15], 2.5)

    def test_fruit_tree_initialization(self):
        ft = FruitTree("Apple Tree")
        self.assertEqual(ft.name, "Apple Tree")
        self.assertTrue(len(ft.harvest_weeks) >= 1)

    def test_vegetable_initialization(self):
        v = Vegetable("Lettuce")
        self.assertEqual(v.name, "Lettuce")
        self.assertTrue(len(v.harvest_weeks) >= 1)