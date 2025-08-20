# Greenhouse temperature control system

# Initial internal temperature adjustment

internal_temp_change = 0  

# Input external conditions
external_temp = float(input("Enter external temperature (°C): "))
sunlight = float(input("Enter sunlight (lux): "))

# Logic
if external_temp < 15 and sunlight < 3000:
    internal_temp_change += 5

elif 15 <= external_temp <= 25:
    if sunlight < 2000:
        internal_temp_change += 3
    elif 2000 <= sunlight <= 4000:
        internal_temp_change += 0
    elif sunlight > 4000:
        internal_temp_change -= 2

elif external_temp > 25:
    if sunlight > 5000:
        internal_temp_change -= 4
    elif 3000 <= sunlight <= 5000:
        internal_temp_change -= 2

# Output
print(f"Temperature change: {internal_temp_change}°C")