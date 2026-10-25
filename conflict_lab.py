def calculate_average(values):
    if not values:
       raise ValueError("Values cannot be empty")
    return sum(values)/len(values)
