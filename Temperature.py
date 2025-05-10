# Matthew Nguyen - Temperature Converter

print("Matthew's Temperature Converter:")

# Prompt user for a temperature and convert to float
fltTemp = float(input("Enter a temperature:"))

# Prompt user for the unit of the temperature
strUnit = input(" Is the temp F for Faherenheit or C for Celsius? ")

# Normalize input to lowercase
strUnit = strUnit.lower()

# Validate input unit
if strUnit not in ('f', 'c'):
    print("You must enter a F or C")
    exit()

# Fahrenheit to Celsius conversion
if strUnit == 'f':
    if fltTemp > 212:
        print("Temp can not be > 212")
    else:
        fltCelsius = (5.0 / 9) * (fltTemp - 32)
        print(f"The Celsius equivalent is: {round(fltCelsius, 1)}")

# Celsius to Fahrenhet conversion
elif strUnit == 'c':
    if fltTemp > 100:
        print("Temp can not be > 100")
    else:
        fltFahrenheit = ((9.0 / 5.0) * fltTemp) + 32
        print(f"The Fahrenheit equivalent is: {round(fltFahrenheit, 1)}")