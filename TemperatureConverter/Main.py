# Constants
FAHRENHEIT_TO_CELSIUS = 5/9
CELSIUS_TO_FAHRENHEIT = 9/5
OFFSET = 32

# User Input
celsius_input = 20
fahrenheit_input = 85

# Conversions
converted_to_F = (celsius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
converted_to_C = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS

# Display
print(f'{celsius_input}°C -> {converted_to_F:.1f}°F')
print(f'{fahrenheit_input}°C -> {converted_to_C:.1f}°F')