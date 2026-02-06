class Plant:
    def __init__(self, name, water, light):
        self.name = name
        self.water = water
        self.light = light

class GardenManager:
    def __init__(self):
        self.plants = []

    def check_plant_health(plant_name, water_level=1, sunlight_hours=2):
        """
        Validates the health conditions of a plant.

        Args:
            plant_name (str): Name of the plant.
            water_level (int): Must be between 1 and 10.
            sunlight_hours (int): Must be between 2 and 12.

        Raises:
            ValueError: If constraints are violated.
        """
        if not plant_name:
            raise ValueError("Error: Plant name cannot be empty!")

        if water_level < 1:
            raise ValueError(
                f"Error: Water level {water_level} is too low (min 1)"
            )
        elif water_level > 10:
            raise ValueError(
                f"Error: Water level {water_level} is too high (max 10)"
            )

        if sunlight_hours < 2:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
            )
        if sunlight_hours > 12:
            raise ValueError(
                f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
            )

        print(f"Plant '{plant_name}' is healthy!")

    def add_plant(self, name, water_level, sunlight):
        print("Adding plants to garden")
        self.check_plant_health(name, water_level, sunlight)
        new_plant = Plant(name, water_level, sunlight)
        self.plants.append(new_plant)
