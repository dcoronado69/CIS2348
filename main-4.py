paintColors = {'red': 35, 'blue':25, 'green': 23}

h = float(input("Enter wall height (feet):\n"))

w = float(input("Enter wall width (feet):\n"))

area = h*w



print("Wall area:",round(area),"square feet")

Gal = area / 350

print("Paint needed:",  '%.2f'% Gal, "gallons")

cans = round(Gal)

print("Cans needed:",cans,"can(s)")

color = input("\nChoose a color to paint the wall:\n")

print("Cost of purchasing "+ color +" paint: $"+str(cans*paintColors[color]))

