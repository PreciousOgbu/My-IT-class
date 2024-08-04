from pillow import Image
Image.open('./Presh.JPG')


def resize_image(img_pth, out_path, width, height):
    image = Image.open(out_path)
    resized_image = image.resize(width, height)
    resized_image.save(out_path)


