# Sample data for appliances: (name, voltage (V), current (A), usage hours/day)
appliances = [
    ("Fan", 220, 0.3, 5),
    ("Refrigerator", 220, 0.8, 24),
    ("TV", 220, 0.5, 4),
    ("LED Bulb", 220, 0.05, 6)
]

print("Appliance Performance Summary:")
total_energy = 0
for name, voltage, current, hours in appliances:
    power = voltage * current  # Power in Watts
    energy_kwh = (power * hours) / 1000  # Energy in kWh
    total_energy += energy_kwh
    print(f"{name}: Voltage={voltage}V, Current={current}A, Power={power:.1f}W, Energy={energy_kwh:.2f}kWh/day")

print(f"\nTotal Daily Energy Consumption: {total_energy:.2f} kWh")
