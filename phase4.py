def optimize_energy(temp):
    if temp > 30:
        mode = "Cooling Mode"
        power = "High"
    elif 20 <= temp <= 30:
        mode = "Eco Mode"
        power = "Medium"
    else:
        mode = "Heating Mode"
        power = "Low"
    return mode, power

# Example usage
temperature = 28  # Example input
mode, power = optimize_energy(temperature)
print(f"Temperature: {temperature}°C")
print(f"Optimized Mode: {mode}")
print(f"Power Level: {power}")
