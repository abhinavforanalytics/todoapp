feet_inches = input("Enter feet and inches: ")


def convert(feet_inches) :
    f, i = map(float, feet_inches.split(' '))
    return f * 0.3048 + i * 0.0254


value = convert(feet_inches)
# print(f'{value:.2f} mts')

if value < 1:
    print("Not allowed on the ride")
else :
    print(f"Enjoy the ride! since the height is {value:.2f}")
