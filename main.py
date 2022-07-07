import PIL.Image
from PIL import Image, ImageDraw, ImageFont, ImageOps

import parametersClass
import schemas


config = parametersClass.Parameters().config

a4 = Image.new("RGB", (2480, 3508), "white")
shape = Image.open(config["shape"].strip())
logo = Image.open(config["logo"].strip()).convert("RGBA")
scheme = shape.copy()
font_lato = ImageFont.truetype(config["font"].strip(), int(config["fontSize"]))

scheme = schemas.create_scheme(shape, logo, int(config["marginTopImg"]), float(config["logoScale"]))

a4 = schemas.create_a4_format(a4,
                              scheme,
                              font_lato,
                              int(config["marginTopText"]),
                              int(config["countStart"]),
                              int(config["countStop"])
                              )
a4.show()
a4.save("stickers.pdf")
