from Servicable import Servicable
from engine.Engine import Engine
from battery.Battery import Battery
from tires.Tyre import Tyre

class Car(Servicable):
    def __init__(self,Engine:Engine,Battery:Battery,Tires:Tyre):
        self._Engine = Engine
        self._Battery = Battery
        self.Tires = Tires

    def needs_service(self)->bool:
        return self._Engine.needs_service() or self._Battery.needs_service() or self.Tires.needs_service()