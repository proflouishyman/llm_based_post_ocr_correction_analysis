from PIL import Image
import glob
import pytesseract
import json
import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("--input_file", dest='input_file', help="input_file_folder")
parser.add_argument("--output_file", dest= "output_file", help = "output_ocr_text")
args = parser.parse_args()

image_dir = args.input_file


for filename in os.listdir(image_dir):
    if not filename.endswith('.txt'):
        print(filename)
        # Construct the full path to the image
        image_path = os.path.join(image_dir, filename)

        # Open the image and perform OCR
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        new_name = filename.strip(".jpg")
        print(new_name)
        file_name = "pytesseract" + new_name + ".txt"
        print(file_name) 
        output_path = os.path.join(args.output_file, file_name) 
        print(output_path)
        with open( output_path, "w") as out_file:
            out_file.write(text)
            print("wrote file!")
