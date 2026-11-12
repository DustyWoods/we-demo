
MIN_WEIGHT = 20.0
MAX_WEIGHT = 300.0

def validate_weight(weight: float):
    '''
    Validate the value

    Raise:
        ValueError: If the value is too low or too high to be true
    '''

    if not MIN_WEIGHT <= weight <= MAX_WEIGHT:
        raise ValueError(
            f"Weight value must be between {MIN_WEIGHT} and {MAX_WEIGHT} kg."

        )

    return round(weight, 1)
