import barcode
from barcode.writer import ImageWriter
from PIL import Image
import datetime
import os
import random

input_text_file = "inputfile.txt"
output_folder = input("Output Folder Title: ")
output_folder_bool = os.path.isdir(output_folder)

while output_folder_bool == True:
    print("Folder with that name already exists.")
    output_folder = input("Output Folder Title: ")
    output_folder_bool = os.path.isdir(output_folder)

possible_colors = ["red", "blue", "green", "orange", "purple", "yellow",]
print("Available colors are:\n\nRed\nBlue\nGreen\nOrange\nPurple\nYellow\n")
color = input("Color: ").lower()

while color not in possible_colors:
    print("Color not valid")
    color = input("Color: ")

input_image_file = os.path.join("templates", color+".png")

if color == "red":
    x_barcode = 288
    y_barcode = 418
elif color == "blue":
    x_barcode = 310
    y_barcode = 416
elif color == "green":
    x_barcode = 334
    y_barcode = 424
elif color == "orange":
    x_barcode = 352
    y_barcode = 429
elif color == "purple":
    x_barcode = 285
    y_barcode = 419
elif color == "yellow":
    x_barcode = 342
    y_barcode = 424
    
number_of_labels = int(input("Number of Labels: "))

prefix = input("Prefix (Letter): ")
starting_number = input("Starting Number: ")
full_code = prefix + starting_number
full_code_length = len(prefix) + len(starting_number)

while full_code_length != 8:
    print("ERROR: Length of barcode must be 8")
    prefix = input("Prefix (Letter): ")
    starting_number = str(input("Starting Number: "))
    full_code = prefix + starting_number
    full_code_length = len(full_code)

finished_folder = "finished"

output_barcodes = "barcodes"
output_labels = "labels"

path1 = os.path.join(finished_folder, output_folder, output_barcodes)
os.makedirs(path1)

path2 = os.path.join(finished_folder, output_folder, output_labels)
os.makedirs(path2)


f = open(input_text_file, "w")
curr_number = starting_number
for i in range(number_of_labels):
    full_code = prefix + curr_number
    f.write(full_code)
    f.write("\n")
    curr_number = str(int(curr_number) + 1)
f.close()
f = open(input_text_file)
# for line in file:
for line in f:

    number = line[:-1]
    leave = input("Press ENTER to continue1")
    # Creates barcode image
    generated_barcode = barcode.get('code128', number, writer=ImageWriter())

    leave = input("Press ENTER to continue2")
    # Sets the barcode image options
    options = dict(text_distance = 2.0, font_size = 25, module_height = 14, module_width = 0.5, mode="RGBA", background="#f4f4f4")
    leave = input("Press ENTER to continue3")
    # Creates the barcode image file path and name
    destination_barcode = os.path.join(finished_folder, output_folder, output_barcodes, number)
    leave = input("Press ENTER to continue4")
    # Saves barcode image
    generated_barcode.save(destination_barcode, options)
    leave = input("Press ENTER to continue5")
    # Opens barcode image as a Pillow object
    barcode_image = Image.open(destination_barcode+".png")
    leave = input("Press ENTER to continue6")
    # Opens label image as Pillow object
    label_image = Image.open(input_image_file)
    leave = input("Press ENTER to continue7")
    # Creates a new blank image with the size of the label image
    final_label = Image.new("RGB",(label_image.size[0], label_image.size[1]))
    leave = input("Press ENTER to continue8")
    # Places label image on blank image, then places barcode on top of label image
    final_label.paste(label_image, (0,0))
    leave = input("Press ENTER to continue9")
    final_label.paste(barcode_image, (x_barcode, y_barcode))
    leave = input("Press ENTER to continue10")
    # Creates the barcode image file path and name
    destination_barcode = os.path.join(finished_folder, output_folder, output_labels, number+".pdf")
    leave = input("Press ENTER to continue11")
    final_label.save(destination_barcode)
    leave = input("Press ENTER to continue12")

leave = input("Press ENTER to continue12")
print("\nSUCCESS!\n")
print("You can find the labels in the programs working directory under the \"finished\" folder")

leave = input("Press ENTER to exit")
