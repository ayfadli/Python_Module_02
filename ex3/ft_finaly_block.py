def water_plants(plant_list):
    """
    Simulates watering plants and ensures the system closes properly.

    Args:
        plant_list (list): List of plant names.

    Raises:
        Exception: If a None value is encountered in the list.
    """
    print("Opening watering system")
    try:
        for plant in plant_list:
            if (plant is None):
                raise Exception(f"Error: Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")

def test_watering_system():
    """
    Tests the watering system with valid and invalid inputs.
    """
    try:
        print("\nTesting normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("\nTesting with error...")
        water_plants(["Tomato", None])
        print("Watering completed successfuly!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
