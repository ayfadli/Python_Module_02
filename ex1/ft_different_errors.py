def garden_operations(error_type):
    """
    Performs different garden operations that intentionally fail
    based on the error_type provided.
    """
    if error_type == "ValueError":
        int("abc")
    elif error_type == "ZeroDivisionError":
        x = 10 / 0
        print(x)
    elif error_type == "FileNotFoundError":
        open("missing.txt")
    elif error_type == "KeyError":
        dict = {
            "brand": "Renault",
            "model": "Koleos",
            "year": 2012
        }
        print(dict["engine"])


def test_error_types():
    """
    Tests specific error types by catching them individually,
    and demonstrates catching multiple errors in one block.
    """
    print("=== Garden Error Types Demo ===")
    print("\nTesting ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("\nTesting KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: 'missing\\_{e}'")
    try:
        print("\nTesting multiple errors together...")
        garden_operations("ValueError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
