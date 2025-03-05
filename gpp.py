import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Centimeters": 0.01, "Meters": 1, "Kilometers": 1000,
        "Millimeters": 0.001, "Nanometers": 1e-9, "Feet": 0.3048
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "Liters": 1, "Milliliters": 0.001, "Cubic Meters": 1000, "Cubic Inches": 0.0163871
    }
    return value * volume_units[from_unit] / volume_units[to_unit]

def convert_area(value, from_unit, to_unit):
    area_units = {
        "Square Meters": 1, "Square Kilometers": 1e6, "Acres": 4046.86, "Hectares": 10000
    }
    return value * area_units[from_unit] / area_units[to_unit]

def convert_mass(value, from_unit, to_unit):
    mass_units = {
        "Grams": 1, "Kilograms": 1000, "Pounds": 453.592, "Ounces": 28.3495
    }
    return value * mass_units[from_unit] / mass_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Unit categories and their options
unit_categories = {
    "Length": ["Centimeters", "Meters", "Kilometers", "Millimeters", "Nanometers", "Feet"],
    "Volume": ["Liters", "Milliliters", "Cubic Meters", "Cubic Inches"],
    "Area": ["Square Meters", "Square Kilometers", "Acres", "Hectares"],
    "Mass": ["Grams", "Kilograms", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Streamlit UI
st.title("Google-Style Unit Converter 🌍")

# Select conversion type
conversion_type = st.selectbox("Select Conversion Type:", list(unit_categories.keys()))

# Select units
from_unit = st.selectbox("From:", unit_categories[conversion_type])
to_unit = st.selectbox("To:", unit_categories[conversion_type])

# Input value
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Perform conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    elif conversion_type == "Area":
        result = convert_area(value, from_unit, to_unit)
    elif conversion_type == "Mass":
        result = convert_mass(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    
    st.success(f"Converted Value: {result:.2f} {to_unit}")
 