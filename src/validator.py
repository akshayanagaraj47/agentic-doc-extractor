def validate_data(data: dict) -> list:
    errors = []

    # Check totals/numbers
    if "total" in data and data["total"]:
        try:
            float(data["total"])
        except:
            errors.append("Total is not a valid number")

    if "amount" in data and data["amount"]:
        try:
            float(data["amount"])
        except:
            errors.append("Amount is not a valid number")

    # Check required fields
    for key, value in data.items():
        if value is None:
            errors.append(f"Missing field: {key}")

    return errors
