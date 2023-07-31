from Servicable import Servicable
from Engine import Engine
from Battery import Battery

class Car(Servicable):
    def __init__(self,Engine:Engine,Battery:Battery):
        self._Engine = Engine
        self._Battery = Battery

    def needs_service(self)->bool:
        return self._Engine.needs_service() or self._Battery.needs_service()