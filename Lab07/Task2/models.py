class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True
        return f"The engine of the {self.brand} {self.model} is now running."

    def stop_engine(self):
        self.engine_started = False
        return f"The engine of the {self.brand} {self.model} has stopped."

    def move(self):
        return "The vehicle is moving."

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, door_count):
        super().__init__(brand, model, year)
        self.door_count = door_count

    def open_trunk(self):
        return f"The trunk of the {self.model} is now open."

    def move(self):
        return f"The {self.model} is driving down the highway."


class ElectricPlane(Vehicle):
    def __init__(self, brand, model, year, max_altitude):
        super().__init__(brand, model, year)
        self.max_altitude = max_altitude

    def check_battery(self):
        return f"Checking battery levels for the {self.brand} flight systems..."

    def move(self):
        return f"The {self.model} is soaring at {self.max_altitude} feet."