## rename.py
Clone rename the files from a source directory to a destination directory setting a rename pattern. Usefull for large image sequences. Of course, it starts from zero.

```python3 rename.py [-z zero_padding_width] src_path dest_path/Output_%n.png```

## compress.py
This compress input images to `webp`. It outputs a summary at the end

```python3 compress.py src_path dest_path --quality 80```

<img width="469" alt="image" src="https://github.com/basementstudio/scripts/assets/43894343/b01eecee-38cc-4d5f-b18c-375bede7b619">

## resize.py
This resizes input images to a target output.

```python3 resize.py src_path dest_path --width 1920 --height 1080```
