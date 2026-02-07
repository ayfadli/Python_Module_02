class GardenError(Exception):
    """Custom exception for garden-related errors."""
    pass


class Plant:
    """Represents a single plant in the garden."""

    def __init__(self, name, water, light):
        self.name = name
        self.water = water
        self.light = light

    def __str__(self):
        return f"{self.name}: healthy (water: {self.water}, sun: {self.light})"


class GardenManager:
    """Manages the garden, including plants and the water tank."""

    def __init__(self):
        self.plants = []
        self.water_tank = 20

    def add_plant(self, name, water_level=1, sunlight=2):
        """
        Add a new plant to the garden after validating conditions.
        """
        try:
            if not name:
                raise ValueError("Plant name cannot be empty!")
            if water_level < 0 or water_level > 10:
                raise ValueError(f"Water level {water_level} is invalid")
            if sunlight < 2 or sunlight > 12:
                raise ValueError(f"Sunlight {sunlight} is invalid")

            new_plant = Plant(name, water_level, sunlight)
            self.plants.append(new_plant)
            print(f"Added {name} successfully")
        except ValueError as e:
            print(f"Error adding plant: {e}")

    def water_all_plants(self):
        """
        Water all plants. Relies on 'finally' for cleanup
        before error propagates.
        """
        print("Opening watering system")
        try:
            for p in self.plants:
                if self.water_tank <= 0:
                    raise GardenError("Not enough water in tank")

                p.water += 5
                self.water_tank -= 5
                print(f"Watering {p.name} - success")

        finally:
            # This runs BEFORE the exception is caught in main
            print("Closing watering system (cleanup)")

    def check_all_health(self):
        """Check and validate the health status of all plants."""
        print("Checking plant health...")
        for p in self.plants:
            try:
                if p.water > 10:
                    raise ValueError(
                        f"Water level {p.water} is too high (max 10)"
                    )
                if p.water < 0:
                    raise ValueError(f"Water level {p.water} is too low")

                print(p)
            except ValueError as e:
                print(f"Error checking {p.name}: {e}")

    def empty_tank(self):
        """Set the water tank level to zero for testing purposes."""
        self.water_tank = 0


if __name__ == "__main__":
    print("=== Garden Management System ===")

    print("Adding plants to garden...")
    ayoub = GardenManager()

    ayoub.add_plant("tomato", water_level=0, sunlight=8)

    ayoub.add_plant("lettuce", water_level=10, sunlight=5)

    ayoub.add_plant("")

    print("Watering plants...")
    ayoub.water_all_plants()

    ayoub.check_all_health()

    print("Testing error recovery...")
    ayoub.empty_tank()
    try:
        ayoub.water_all_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")
