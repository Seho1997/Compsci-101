"""
Name: Se Ho Lee
Username: slee626
Student Id: 890218467
Description: A Program that calculates the surface area and volume of a right regular octagonal prism. (3 Marks)
"""
first_line_description = "Right Regular Octagonal Prism"
second_line_description = "Surface Area and Volume Calculator"
front_extras = 2
end_extras = 3
full_length = len(second_line_description)
border_line_length = full_length

print("*" * border_line_length)
print(" " * front_extras + first_line_description + " " * end_extras)
print(second_line_description)
print("*" * border_line_length)
print("")

base_edge = int(input("Base Edge: "))
height = int(input("Height: "))
print("")

surface_area = (8 * base_edge * height + 4 * (1 + 2 ** 0.5) * base_edge ** 2)
volume = 2 * (1 + 2 ** 0.5) * base_edge ** 2 * height

print("Surface Area:", round(surface_area,3))
print("Volume:", round(volume,3))
