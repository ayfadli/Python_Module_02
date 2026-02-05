def water_plants(plant_list):
    print("Opening watering system")
    for plant in plant_list:
        print(f"Watering {plant}")
    print("Closing watering system (cleanup)")


def test_watering_system():
    try:
        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfuly!")
    except :
        print("Error: Cannot water None - invalid plant!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")
