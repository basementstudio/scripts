import os
import argparse
from PIL import Image

def resize_images(input_dir, output_dir, width, height):
    """
    Resize images in the input directory and save them to the output directory.
    
    Args:
        input_dir (str): Path to the input directory containing images.
        output_dir (str): Path to the output directory to save resized images.
        width (int): Desired width of the resized images.
        height (int): Desired height of the resized images.
    """
    supported_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(ext) for ext in supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            with Image.open(input_path) as img:
                resized_img = img.resize((width, height), Image.LANCZOS)
                resized_img.save(output_path)
                print(f"Resized {filename} and saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Resize images to specified dimensions")
    parser.add_argument('input_dir', type=str, help="Path to the input directory containing images")
    parser.add_argument('output_dir', type=str, help="Path to the output directory to save resized images")
    parser.add_argument('--width', type=int, required=True, help="Desired width of the resized images")
    parser.add_argument('--height', type=int, required=True, help="Desired height of the resized images")

    args = parser.parse_args()
    resize_images(args.input_dir, args.output_dir, args.width, args.height)

if __name__ == "__main__":
    main()