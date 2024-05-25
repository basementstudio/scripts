import os
import argparse
from PIL import Image

def compress_images_to_webp(input_dir, output_dir, quality=80):
    """
    Compress all images in the input directory to WebP format and save them to the output directory.
    
    Args:
        input_dir (str): Path to the input directory containing images.
        output_dir (str): Path to the output directory to save compressed images.
        quality (int): Quality setting for the compressed images (0-100).
    """
    supported_formats = ['jpg', 'jpeg', 'png', 'bmp', 'tiff', 'webp']

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(ext) for ext in supported_formats):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.webp')
            
            with Image.open(input_path) as img:
                img.save(output_path, 'webp', quality=quality)
                print(f"Compressed {filename} and saved as {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Compress images to WebP format")
    parser.add_argument('input_dir', type=str, help="Path to the input directory containing images")
    parser.add_argument('output_dir', type=str, help="Path to the output directory to save compressed images")
    parser.add_argument('--quality', type=int, default=80, help="Quality setting for the compressed images (0-100)")

    args = parser.parse_args()
    compress_images_to_webp(args.input_dir, args.output_dir, args.quality)

if __name__ == "__main__":
    main()