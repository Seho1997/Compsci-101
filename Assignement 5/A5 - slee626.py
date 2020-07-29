"""
Name: Se Ho Lee
Username: slee626
ID Number: 890218467
Description: This program is a program that reads informations from several text files to dispay shapes.
"""

from tkinter import *

#-------------------------------------------
# -- Returns a colours dictionary
#-------------------------------------------
def create_colours_dictionary(filename):
     colours_dict = {}
     variable_file = open(filename, 'r')
     file_content = variable_file.read()
     variable_file.close()
     file_list = file_content.split()
     for name in file_list:
          divider = name.find(":")
          colours_dict.update({int(name[:divider]) : name[divider + 1:]})

     return colours_dict
	
#-------------------------------------------
# -- Returns a list of filenames
#-------------------------------------------
def create_filenames_list(filename):
     filenames_list = []
     variable_file = open(filename, 'r')
     file_content = variable_file.read()
     variable_file.close()
     filenames_list = file_content.split()
     return filenames_list
	
#-------------------------------------------
# -- Reads the coordinates from the input file
#-------------------------------------------
def read_coordinates(filename, shapes_dict):
     coordinates_file = open(filename, 'r')
     read_coordinates = coordinates_file.read()
     coordinates_file.close()
     coordinates_list = read_coordinates.split()
     for numbers in range(len(coordinates_list)):
          coordinates_list[numbers] = coordinates_list[numbers].split(",")
          shapes_dict[len(coordinates_list[numbers]) // 2] = coordinates_list[numbers]

     print(shapes_dict)	
#-------------------------------------------
# -- Draws all shapes
#-------------------------------------------
def draw_shapes(canvas, colours_dict, shapes_dict):
     for value in shapes_dict:
         if value == 2:
             canvas.create_rectangle(shapes_dict[value], fill = colours_dict[value])
         else:
             canvas.create_polygon(shapes_dict[value], fill = colours_dict[value])
         
     print()





#------------------------------------------
# MAKE ONE CHANGE TO THE MAIN FUNCTION
#------------------------------------------
def main():
	window = Tk()
	window.title("A5 - slee626")
	window.geometry("600x600")
	a_canvas = Canvas(window)
	a_canvas.pack(fill=BOTH, expand=True)

	colours_dict = create_colours_dictionary('colours.txt')
	print(colours_dict)

	shapes_dict = {}
	for key in colours_dict.keys():
		shapes_dict[key] = []

	filenames_list = create_filenames_list('input.txt')
	print(filenames_list)

	for filename in filenames_list:
	      read_coordinates(filename, shapes_dict)
	      draw_shapes(a_canvas, colours_dict, shapes_dict)

	window.mainloop()

main()
