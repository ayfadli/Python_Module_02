def check_temperature(temp_str):
    """
    Takes a string input, validates it as a number, and checks if it
    is within the safe range for plants (0-40).
    Returns the temperature if valid, otherwise handles errors.
    """
    try:
        temp_val = int(temp_str)

        if temp_val < 0:
            print(f"Error: {temp_val}°C is too cold for plants (min 0°C)")
        elif temp_val > 40:
            print(f"Error: {temp_val}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_val}°C is perfect for plants!")
            return temp_val

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """
    Runs a series of tests to demonstrate the robustness of the
    check_temperature function against various inputs.
    """
    print("Testing temperature: 25")
    check_temperature("25")

    print("Testing temperature: abc")
    check_temperature("abc")

    print("Testing temperature: 100")
    check_temperature("100")

    print("Testing temperature: -50")
    check_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
    print("All tests completed - program didn't crash!")
