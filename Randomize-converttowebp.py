import os
import random
import string
from shutil import rmtree
from PIL import Image

source_directory = input("Enter the source directory: ")

if not os.path.isdir(source_directory):
    print("Invalid source directory!")
    exit()

output_directory = os.path.join(source_directory, "WebP")

if os.path.exists(output_directory):
    rmtree(output_directory)

os.makedirs(output_directory)

for file_name in os.listdir(source_directory):
    file_path = os.path.join(source_directory, file_name)
    if os.path.isfile(file_path):
        filename, file_extension = os.path.splitext(file_name)
        filename_lowercase = filename.lower()
        random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=18))
        output_file = os.path.join(output_directory, random_name + ".webp")

        # Use PIL library to convert the image to WebP format
        img = Image.open(file_path)
        img.save(output_file, "webp")

        # Alternatively, you can use the `convert` command from ImageMagick
        # command = f"convert {file_path} {output_file}"
        # os.system(command)
