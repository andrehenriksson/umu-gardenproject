import unittest
from garden import GardenContainer
from plant import Plant
from pest import Pest

class TestGardenContainer(unittest.TestCase):
    def setUp(self):
        return super().setUp()
 
    def tearDown(self):
        return super().tearDown()
 
    def test_add_plant(self):
        garden = GardenContainer()
        p = Plant("Cabbage")
        garden.add_plant(p)
        self.assertIn("Cabbage", garden.plants)

    def test_add_pest(self):
        garden = GardenContainer()
        pest_obj = Pest("Ants", "Vegetable", 20)
        garden.add_pest(pest_obj)
        self.assertIn("Ants", garden.pests)