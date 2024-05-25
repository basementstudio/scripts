import os
import argparse
import shutil
import tempfile

def parse_arguments():
    parser = argparse.ArgumentParser(description="Copy and rename files with zero padding.")
    parser.add_argument('-z', type=int, default=2, help="Zero padding width")
    parser.add_argument('src_path', type=str, help="Source directory path")
    parser.add_argument('target_pattern', type=str, help="Target pattern with path (e.g., /path/to/destination/Comp_%n.png)")
    return parser.parse_args()

def main():
    args = parse_arguments()
    zero_padding_width = args.z
    src_path = args.src_path
    target_pattern_with_path = args.target_pattern

    if not os.path.isdir(src_path):
        print(f"Source directory does not exist: {src_path}")
        exit(1)

    target_directory = os.path.dirname(target_pattern_with_path)

    if not os.path.isdir(target_directory):
        print(f"Target directory does not exist: {target_directory}")
        exit(1)

    target_pattern = os.path.basename(target_pattern_with_path)
    tmp_dir = tempfile.mkdtemp()

    try:
        if os.listdir(src_path):
            counter = 0
            for filename in os.listdir(src_path):
                file_path = os.path.join(src_path, filename)
                if os.path.isdir(file_path):
                    continue

                extension = filename.split('.')[-1]
                formatted_counter = f"{counter:0{zero_padding_width}d}"
                new_file = target_pattern.replace('%n', formatted_counter)

                if not new_file.endswith(f".{extension}"):
                    new_file = f"{new_file}.{extension}"

                new_file_path = os.path.join(tmp_dir, new_file)
                shutil.copy(file_path, new_file_path)
                print(f"Prepared to copy: {file_path} -> {new_file_path}")
                counter += 1

            for filename in os.listdir(tmp_dir):
                shutil.move(os.path.join(tmp_dir, filename), target_directory)
            print("All files successfully copied and renamed.")
        else:
            print("No files found in the source directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        shutil.rmtree(tmp_dir)

if __name__ == "__main__":
    main()