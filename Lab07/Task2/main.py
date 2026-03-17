from models import Car, ElectricPlane

def main():
    my_car = Car("Tesla", "Model 3", 2024, 4)
    my_plane = ElectricPlane("Airbus", "E-Fan X", 2025, 30000)

    fleet = [my_car, my_plane]

    print("--- Vehicle Fleet Report ---")
    
    for vehicle in fleet:
        print(f"\nVehicle: {vehicle}")
        print(vehicle.start_engine())
        
        print(f"Action: {vehicle.move()}")
        
        if isinstance(vehicle, Car):
            print(vehicle.open_trunk())
        elif isinstance(vehicle, ElectricPlane):
            print(vehicle.check_battery())

if __name__ == "__main__":
    main()