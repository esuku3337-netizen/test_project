def calculate_average(values):
    if not values:
        raise ValueError("Values cannot be empty")

    return sum(values) / len(values)


def summarize_project():
    return "This is our first git project"
