"""
Interface Segregation Principle: "Many client-specific interfaces are better than one general-purpose interface"
"""


class EngineInterface:

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError


class Car:

    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

    def stop(self):
        self.engine.stop()


class ElectricEngine(EngineInterface):

    def start(self):
        pass
        # Starting the electric motor

    def stop(self):
        pass
        # Stopping the electric motor


class GasolineEngine(EngineInterface):

    def start(self):
        pass
        # Starting the gasoline motor

    def stop(self):
        pass
        # Stopping the gasoline motor
