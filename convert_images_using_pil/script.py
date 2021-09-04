#!/usr/bin/env python3
import os
from PIL import Image

def load_images(folder):
    images = os.listdir(folder)
    jpeg_format = os.mkdir("jpeg_images")
    dest = os.path.join("images", "jpeg_format")
    try:
        for image in images:
            with Image.open(folder+image) as img:
                new_image = img.rotate(90)
                new_image = img.resize((128,128))
                new_image.save(dest,"JPEG")
                return new_image
    except OSError as e:
        print(e)

if __name__ == '__main__':
    dir = load_images("/Users/ranjan/pythonCodes/fun_with_python/convert_images_using_pil/images/")
