# 24127448 - Le Duc Minh

import os

filename = "filenamehere.extension"

if os.path.exists(filename):
    with open(filename, "r") as file:
        content = file.read()
        print(content)
else:
    print("file doesn't exist")