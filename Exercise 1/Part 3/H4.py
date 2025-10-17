# 24127448 - Le Duc Minh

import os

filename = input("Enter your file (format: filename.extension): ") # If not in folder then do foldername\filename.extension (can be multiple folder, example Exercise 1\Part 3\H2.py)

if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print("file doesn't exist")