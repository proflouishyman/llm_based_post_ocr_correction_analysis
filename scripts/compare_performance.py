import argparse
import os 
import jiwer
from jiwer import wer, cer 
import json

parser = argparse.ArgumentParser()

parser.add_argument("--control_directory", dest='control_directory', help="ground truth file_folder")
parser.add_argument("--test_directory", dest= "test_directory", help = "test file folder")
parser.add_argument("--output_file", dest = "output_folder", help = "where the output goes", required = True)


args = parser.parse_args()
control_files = []
test_files = []

for filename in os.listdir(args.control_directory):
    if filename.endswith('.txt'):
        control_files.append(filename)        


#for filename in os.listdir(args.test_directory):
 #   if filename.endswith('.txt'):
  #      test_files.append(filename)

for filename in os.listdir(args.test_directory):                                                                                                                                                
    if filename.endswith('.txt'):                                                                                                                                                               
        test_files.append(filename) 

        
output_dictionary = {}

for entry in test_files:
    entry_name = entry.lstrip("pytesseract")
    for x in control_files:
        if entry_name == x:
            with open(os.path.join(args.test_directory, entry), "r") as test_file, open (os.path.join(args.control_directory,x), "r") as control_file:
                test_text = test_file.read()
                control_text = control_file.read()
                #output = jiwer.process_words(control_text, test_text)
                #error = output.cer
                error = cer(control_text, test_text)
                local_dict = {"control_text" : control_text, "pytesseract_text" : { "text" : test_text, "CER" : error}}
                output_dictionary[x] = local_dict 

                        
with open (args.output_folder, "w") as out_file:
    json.dump(output_dictionary, out_file, indent = 4)

