from PIL import Image, ImageDraw, ImageFont, ImageOps


def create_scheme(base, img, pos_y, scale):
    w_shape, h_shape = base.size
    w, h = img.size

    img = img.resize((int(w_shape * scale), int(w_shape / w * h * scale)))

    base.paste(img, (int(w_shape / 2 - img.size[0] / 2), pos_y), img)

    return base


def create_from_schema(base, text, font, height):
    tmp_scheme = base.copy()
    add_text(text, font, tmp_scheme, height)

    return tmp_scheme


def add_text(text, font, img, pos_y):
    d1 = ImageDraw.Draw(img)
    w, h = d1.textsize(text, font=font)
    d1.text((int((img.size[0] - w) / 2), pos_y), text, font=font, fill=(0, 0, 0), align="center")


def create_a4_format(a4_base, base_schema, font, height, countStart, countStop):
    position = [0, 0]
    for i in range(countStart, countStop + 1):
        tmp = create_from_schema(base_schema, str(i), font, height)
        a4_base.paste(tmp, (position[0], position[1]), tmp)
        if a4_base.size[0] < position[0] + base_schema.size[0] * 2:
            position[0] = 0
            position[1] += base_schema.size[1]
        else:
            position[0] += base_schema.size[0]

    return a4_base
