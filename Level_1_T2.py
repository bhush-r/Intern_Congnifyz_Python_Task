temperature = float(input("Enter the temperature value: "))
#This line asks the user to enter the temp value and stores it in the variable `temperature`.input string to a floating-point number

unit = input("Enter the unit of measurement (C for Celsius, F for Fahrenheit): ")
# This line asks the user to enter the unit of measurement and stores it in the variable `unit`.

if unit.upper() == "C":
# This line checks if the unit of measurement is Celsius. If it is, the code converts the temperature to Fahrenheit and prints the result.
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature}°F")
elif unit.upper() == "F":
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature}°C")
else:
# This line prints an error message if the unit of measurement is invalid.
    print("Invalid unit of measurement.") 