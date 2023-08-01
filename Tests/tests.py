import unittest
from datetime import datetime

from engine.CapuletEngine.CapuletEngine import CapuletEngine
from engine.WilloughbyEngine.WilloughbyEngine import WilloughbyEngine
from engine.SternmanEngine.SternmanEngine import SternmanEngine

from battery.NubbinBattery.NubbinBattery import NubbinBattery
from battery.SplindlerBattery.SplindlerBattery import SplindlerBattery

class CapuletEngineTest(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30000
        engine = CapuletEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())

class WilloughbyEngineTest(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60000
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        self.assertFalse(engine.needs_service())

class SternmanEngineTest(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())

class SplindlerBatteryTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)
        battery = SplindlerBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service()) 

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        battery = SplindlerBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service()) 

class NubbinBatteryTest(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        battery = NubbinBattery(current_date,last_service_date)
        self.assertTrue(battery.needs_service()) 

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 2)
        battery = NubbinBattery(current_date,last_service_date)
        self.assertFalse(battery.needs_service())

if (__name__ == '__main__'):
    unittest.main()