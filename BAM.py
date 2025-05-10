# Prompt user for name and Earth Wieght
s_name = input("What is your name?")
f_earth_weight = float(input("What is your wieght?"))


#Define  varibles for gravity factors

GRAVITY_MERCURY = 0.38
GRAVITY_VENUS = 0.91
GRAVITY_MOON = 0.165
GRAVITY_MARS = 0.38
GRAVITY_JUPITER = 2.34
GRAVITY_SATURN = 0.93
GRAVITY_URANUS = 0.92
GRAVITY_NEPTUNE = 1.12
GRAVITY_PLUTO = 0.066

# Calculating wieghts on different planets
f_weight_mercury= wieght = f_earth_weight * GRAVITY_MERCURY
f_weight_venus= f_earth_weight * GRAVITY_VENUS
f_weight_moon= f_earth_weight  * GRAVITY_MOON
f_weight_mars = f_earth_weight * GRAVITY_MARS
f_weight_jupiter = f_earth_weight * GRAVITY_JUPITER
f_weight_saturn = f_earth_weight * GRAVITY_SATURN
f_weight_uranus  = f_earth_weight * GRAVITY_URANUS
f_weight_neptune = f_earth_weight * GRAVITY_NEPTUNE
f_weight_pluto = f_earth_weight * GRAVITY_PLUTO

#Display planet wieghts

print(f"{'Planet':<10}{'Weight (lbs)':>15}")
print("-" * 25)
print(f"{'Mercury':<10}{f_weight_mercury:>15.2f}")
print(f"{'Venus':<10}{f_weight_venus:>15.2f}")
print(f"{'Moon':<10}{f_weight_moon:>15.2f}")
print(f"{'Mars':<10}{f_weight_mars:>15.2f}")
print(f"{'Jupiter':<10}{f_weight_jupiter:>15.2f}")
print(f"{'Saturn':<10}{f_weight_saturn:>15.2f}")
print(f"{'Uranus':<10}{f_weight_uranus:>15.2f}")
print(f"{'Neptune':<10}{f_weight_neptune:>15.2f}")
print(f"{'Pluto':<10}{f_weight_pluto:>15.2f}")
