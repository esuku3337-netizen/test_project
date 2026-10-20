def calculate_average(values:list[float])->float:
    """Calculate the average of a non-empty list of numbers."""
    if not values:
        raise ValueError("Values cannot be empty")

    return sum(values) / len(values)


def summarize_project():
    """Return a short description of the project."""
    return "This is our first git project"
