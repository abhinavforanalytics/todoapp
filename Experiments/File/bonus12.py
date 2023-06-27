from Experiments.File.Parsers import parse
from Experiments.File.Converters import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)
value = convert(parsed['Feet'], parsed['Inches'])

if value < 1:
    print("Not allowed on the ride")
else:
    print(f"Enjoy the ride! since the height is {value:.2f}mts or {parsed['Feet']} feet and {parsed['Inches']} inches")
