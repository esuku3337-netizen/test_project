def calculate_average(values):
    if not values:
       raise ValueError("Values cannot be empty")
    return round(sum(values)/len(values),2)
