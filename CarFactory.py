from datetime import date

import Car

from engine.CapuletEngine.CapuletEngine import CapuletEngine
from engine.WilloughbyEngine.WilloughbyEngine import WilloughbyEngine
from engine.SternmanEngine.SternmanEngine import SternmanEngine

from battery.SplindlerBattery.SplindlerBattery import SplinderBattery
from battery.NubbinBattery.NubbinBattery import NubbinBattery

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool)->Car:
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine,battery)
    
    @staticmethod
    def  create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) ->Car :
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        return Car(engine,battery)