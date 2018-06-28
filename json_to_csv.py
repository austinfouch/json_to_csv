## Author:  Austin Fouch
## Date:    06/27/2018
## Simple JSON to CSV converter that uses first level keys as headers
import csv
import json
import tkinter as tk
import ctypes
import sys
from tkinter import filedialog

# prompt JSON file from windows explorer
root = tk.Tk()
root.withdraw()
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Select a file with JSON data', 'json_to_csv', 0)
jsonFilePath = filedialog.askopenfilename()

# load json file into list of dicts
while True:
    try:
        with open(jsonFilePath) as f:
            jsonData = json.load(f)
            break
    except json.decoder.JSONDecodeError:
        MessageBox(None, 'Not valid JSON data, select a file with valid JSON data', 'Error', 0)
        jsonFilePath = filedialog.askopenfilename()

# grab column headers from jsonData
columns = set([i for s in [d.keys() for d in jsonData] for i in s])

# select output file and write csv
MessageBox(None, 'Select/Create a file to store CSV data', 'json_to_csv', 0)
outputFile = filedialog.askopenfilename()
with open(outputFile, 'w') as outfile:
    mywriter = csv.DictWriter(outfile, delimiter=',', lineterminator='\n', fieldnames=columns)
    mywriter.writeheader()

    mywriter.writerows(jsonData)
MessageBox(None, 'CSV data written to ' + outputFile, 'json_to_csv', 0)