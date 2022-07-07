import PIL.ImageOps
from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys


def create_scheme(base, img, pos_y, scale):
    w_shape, h_shape = base.size
    w, h = img.size

    img = img.resize((int(w_shape * scale), int(w_shape / w * h * scale)))
    mask = create_mask_from_shape(base).convert("L")

    base.paste(img, (int(w_shape / 2 - img.size[0] / 2), pos_y), img)

    base.putalpha(mask)

    mask = mask.resize((mask.size[0]+2, mask.size[1]+2))
    mask = PIL.ImageOps.invert(mask)
    mask = mask.convert("RGBA")
    mask.paste(base, (int((mask.size[0]-base.size[0])/2), int((mask.size[1]-base.size[1])/2)), base)
    return mask


def create_mask_from_shape(shape):
    mask = shape.copy().convert("RGBA")
    width = mask.size[0]
    height = mask.size[1]
    for i in range(0, width):  # process all pixels
        for j in range(0, height):
            data = mask.getpixel((i, j))
            # print(data) #(255, 255, 255)
            if (data[0] != 255 and data[1] != 255 and data[2] != 255):
                mask.putpixel((i, j), (0, 0, 0))

    return mask


def create_from_schema(base, text, font, height):
    tmp_scheme = base.copy()
    add_text(text, font, tmp_scheme, height)

    return tmp_scheme


def add_text(text, font, img, pos_y):
    d1 = ImageDraw.Draw(img)
    w, h = d1.textsize(text, font=font)
    d1.text((int((img.size[0] - w) / 2), pos_y), text, font=font, fill=(0, 0, 0), align="center")


def create_a4_format(a4_base, base_schema, font, height, countStart, countStop):
    start_position = (50, 50)
    position = [start_position[0], start_position[1]]
    for i in range(countStart, countStop + 1):
        tmp = create_from_schema(base_schema, str(i), font, height)
        if a4_base.size[1] < position[1] + base_schema.size[1]:
            return a4_base

        a4_base.paste(tmp, (position[0], position[1]), tmp)

        if a4_base.size[0] < position[0] + base_schema.size[0] * 2:
                position[0] = start_position[0]
                position[1] += base_schema.size[1] + 10
        else:
            position[0] += base_schema.size[0] + 10

    return a4_base
