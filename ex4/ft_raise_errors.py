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


def test_plant_check():
    """
    Runs a series of tests to verify exception handling.
    """
    try:
        print("\nTesting good values...")
        check_plant_health("tomato")
    except ValueError as e:
        print(e)

    try:
        print("\nTesting empty plant name...")
        check_plant_health("", 2, 7)
    except ValueError as e:
        print(e)

    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15)
    except ValueError as e:
        print(e)

    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===")
    test_plant_check()
