# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:
    def __init__(self, name):


class GroundVehicle(Vehicle):
    def __init__(self, name, gas_type):
        super().__init__(name)
        self.gas_type = gas_type

class Car(GroundVehicle):
    def __init__(self, name, gas_type, make, model):
        super().__init__(name, gas_type)
        self.make = make
        self.model = model

class Motorcycle(GroundVehicle):
    def __init__(self, name, gas_type, model):
        super().__init__(name, gas_type)
        self.model = model

class FlightVehicle(Vehicle):
    def __init__(self, name, engine_size):
        super().__init__(name)
        self.engine_size = engine_size

class Airplane(FlightVehicle):
    def __init__(self, name, engine_size, passenger_total):
        super().__init__(name, engine_size)
        self.passenger_total = passenger_total

class Starship(FlightVehicle):
    def __init__(self, name, engine_size, successful_flights):
        super().__init__(name, engine_size)
        self.successful_flights = successful_flights