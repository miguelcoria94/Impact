import os
# pip install pillow

from flask import url_for, current_app
from PIL import Image


def add_post_image(pic_upload, posttile):

    filename = pic_upload.filename
    # Grab extension type .jpg or .png
    ext_type = filename.split('.')[-1]
    storage_filename = str(posttitle) + '.' + ext_type
    filepath = os.path.join(current_app.root_path,
                            'static/post_pics', storage_filename)

    # Play Around with this size.
    output_size = (1920, 1080)

    # Open the picture and save it
    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    print(storage_filename)

    return storage_filename
