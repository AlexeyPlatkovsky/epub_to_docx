import os

from PIL import Image


def convert_webp_to_png(input_path, output_path):
    # Open the WEBP image
    img = Image.open(input_path)

    # Save as PNG
    img.save(output_path, "PNG")
    print(f"Conversion successful: {output_path}")


# Define the input and results directories
input_folder = './../input_image_files'
results_folder = './../results_image'

# Create the results folder if it doesn't exist
if not os.path.exists(results_folder):
    os.makedirs(results_folder)


for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.webp', '.jpeg', '.jpg', '.bmp', '.svg')):
        webp_file = os.path.join(input_folder, filename)
        # Construct the output DOCX file path using the same base filename
        base_name = os.path.splitext(filename)[0]
        png_file = os.path.join(results_folder, base_name + '.png')
        # Only convert if the DOCX does not already exist
        if not os.path.exists(png_file):
            print(f"Converting '{filename}' to PNG...")
            convert_webp_to_png(webp_file, png_file)
        else:
            print(f"Skipping '{filename}' (PNG already exists).")