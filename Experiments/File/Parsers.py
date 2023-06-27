def parse(feet_inches) :
    f, i = map(float, feet_inches.split(' '))
    return {"Feet": f, "Inches": i}


