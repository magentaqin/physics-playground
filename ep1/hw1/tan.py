import math
# earth question
# earth_radius = 6.378 * pow(10,6)
# distance = 4.3 * pow(10,16)
# arc_tan_radians = 2 * math.atan(earth_radius/distance)
# print(arc_tan_radians)

# raindrop question
cylinder_volume = 3000 * math.pi * 1000 * 1000
radius = pow(10,-5)
bound_l = cylinder_volume * 4/3 * math.pi * pow(radius, 3) * 50 * pow(10,6)
print('low', bound_l * 1000)
bound_h = cylinder_volume * 4/3 * math.pi * pow(radius, 3) * 500 * pow(10,6)
print('high', bound_h)
