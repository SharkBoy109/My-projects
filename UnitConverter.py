def convert_length(value, from_unit, to_unit):
    units = {
        'm': 1,         # meter
        'km': 1000,     # kilometer
        'cm': 0.01,     # centimeter
        'mm': 0.001,    # millimeter
        'mile': 1609.34, # mile
        'yard': 0.9144,  # yard
        'foot': 0.3048,  # foot
    }
    
    # Convert to meters first, then to target unit
    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid units.")
    
    value_in_meters = value * units[from_unit]
    return value_in_meters / units[to_unit]

def convert_mass(value, from_unit, to_unit):
    units = {
        'kg': 1,         # kilogram
        'g': 0.001,      # gram
        'mg': 0.000001,  # milligram
        'ton': 1000,     # ton
        'lb': 0.453592,   # pound
        'oz': 0.0283495,  # ounce
    }

    if from_unit not in units or to_unit not in units:
        raise ValueError("Invalid units.")
    
    value_in_kg = value * units[from_unit]
    return value_in_kg / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return value * 9/5 + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9/5 + 32
    else:
        raise ValueError("Invalid temperature units.")

def unit_converter(value, from_unit, to_unit, category):
    if category == 'length':
        return convert_length(value, from_unit, to_unit)
    elif category == 'mass':
        return convert_mass(value, from_unit, to_unit)
    elif category == 'temperature':
        return convert_temperature(value, from_unit, to_unit)
    else:
        raise ValueError("Invalid category.")

# Example Usage:
value = 100
from_unit = 'km'
to_unit = 'm'
category = 'length'

result = unit_converter(value, from_unit, to_unit, category)
print(f"{value} {from_unit} = {result} {to_unit}")
