import os
import sys
from PIL import Image, ImageOps


extensions = [".jpg", ".jpeg", ".png"]

if len(sys.argv) != 3:
    sys.exit(1)
if not os.path.exists(sys.argv[1]):
    sys.exit(1)

inp = sys.argv[1]
out = sys.argv[2]

if not any(inp.lower().endswith(e) for e in extensions) or not any(out.lower().endswith(e) for e in extensions):
    sys.exit(1)
if inp.split(".")[-1] != out.split(".")[-1]:
    sys.exit(1)

try:
    shirt = Image.open("shirt.png")
    unresized_inp_image = Image.open(inp)

    inp_image = ImageOps.fit(unresized_inp_image, shirt.size)

    inp_image.paste(shirt, (0, 0), shirt)

    inp_image.save(out)

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
