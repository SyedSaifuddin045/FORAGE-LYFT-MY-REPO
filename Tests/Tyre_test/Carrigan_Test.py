import unittest
from tires.Carrigan import Carrigan

class OctoPrimeTest(unittest.TestCase):
    def test_tyre_should_be_serviced(self):
        tire_wear = [0.1,0.7,0.6,0.9]
        tyre = Carrigan(tire_wear)
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tire_wear = [0.1,0.2,0.3,0.1]
        tyre = Carrigan(tire_wear)
        self.assertFalse(tyre.needs_service())