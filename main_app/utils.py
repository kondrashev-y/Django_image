from PIL import Image


def resize_image(instance, width=None, height=None):
    with Image.open(instance.image) as im:
        w, h = im.size

        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)
        else:
            return None
        im.thumbnail(max_size, Image.ANTIALIAS)
        im.save(instance.custom_image.path, im.format)
