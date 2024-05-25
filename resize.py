import os
import argparse
from PIL import Image

def resize_images(input_dir, output_dir, width=None, height=None, scale=None):
    """
    Resize images in the input directory and save them to the output directory.
    
    Args:
        input_dir (str): Path to the input directory containing images.
        output_dir (str): Path to the output directory to save resized images.
        width (int, optional): Desired width of the resized images.
        height (int, optional): Desired height of the resized images.
        scale (float, optional): scale factor for the images.
    """
    supported_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(ext) for ext in supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            with Image.open(input_path) as img:
                if scale:
                    width = int(img.width * scale)
                    height = int(img.height * scale)
                elif not width or not height:
                    print(f"Skipping {filename}: Either width or height is missing.")
                    continue

                resized_img = img.resize((width, height), Image.LANCZOS)
                resized_img.save(output_path)
                print(f"Resized {filename} and saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Resize images to specified dimensions or scale by a factor.")
    parser.add_argument('input_dir', type=str, help="Path to the input directory containing images")
    parser.add_argument('output_dir', type=str, help="Path to the output directory to save resized images")
    parser.add_argument('--width', type=int, help="Desired width of the resized images")
    parser.add_argument('--height', type=int, help="Desired height of the resized images")
    parser.add_argument('--scale', type=float, help="scale factor for the images")

    args = parser.parse_args()
    if not args.scale and (not args.width or not args.height):
        parser.error("Either --scale or both --width and --height must be specified.")

    resize_images(args.input_dir, args.output_dir, args.width, args.height, args.scale)

if __name__ == "__main__":
    main()