# converter.py

def celsius_to_fahrenheit(c):
    return round(c * 9/5 + 32, 2)

def fahrenheit_to_celsius(f):
    return round((f - 32) * 5/9, 2)

def km_to_miles(km):
    return round(km * 0.621371, 2)

def miles_to_km(miles):
    return round(miles / 0.621371, 2)

def kg_to_libras(kg):
    return round(kg * 2.20462, 2)

def libras_to_kg(lb):
    return round(lb / 2.20462, 2)