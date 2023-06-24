feet_inches = input("Enter feet and inches: ")


def parse(feet_inches) :
    f, i = map(float, feet_inches.split(' '))
    return {"Feet" : f, "Inches" : i}


def convert(feet, inches) :
    return feet * 0.3048 + inches * 0.0254


parsed = parse(feet_inches)
value = convert(parsed['Feet'],parsed['Inches'])
# print(f'{value:.2f} mts')

if value < 1:
    print("Not allowed on the ride")
else :
    print(f"Enjoy the ride! since the height is {value:.2f}mts or {parsed['Feet']} feet and {parsed['Inches']} inches")
