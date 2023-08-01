from battery.Battery import Battery

from datetime import date

class SplindlerBattery(Battery):
    def __init__(self,current_date:date,last_service_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        if (self.current_date.year - self.last_service_date.year > 2) :
            return True
        else:
            return False