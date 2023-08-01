from datetime import date

import Car

from engine.CapuletEngine.CapuletEngine import CapuletEngine
from engine.WilloughbyEngine.WilloughbyEngine import WilloughbyEngine
from engine.SternmanEngine.SternmanEngine import SternmanEngine

from battery.SplindlerBattery.SplindlerBattery import SplinderBattery
from battery.NubbinBattery.NubbinBattery import NubbinBattery

from tires.Carrigan import Carrigan
from tires.Octoprime import Octoprime

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int,tire_wear) -> Car:
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        tyre = tire_wear 
        return Car(engine,battery,tyre)
    
    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int,tire_wear) -> Car:
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SplinderBattery(current_date,last_service_date)
        tyre = tire_wear 
        return Car(engine,battery,tyre)
    
    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool,tire_wear)->Car:
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(current_date,last_service_date)
        tyre = tire_wear 
        return Car(engine,battery,tyre)
    
    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int,tire_wear) -> Car:
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tyre = tire_wear 
        return Car(engine,battery,tyre)
    
    @staticmethod
    def  create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int,tire_wear) ->Car :
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tyre = tire_wear 
        return Car(engine,battery,tyre)