from PIL import Image

def apply_color_bits(image_path, color, outfile):
    img = Image.open(image_path).convert("RGB")
    rC, gC, bC = color   # given color

    # highest 2 bits (00xxx000 → keep only top 2)
    r2 = (rC >> 6) & 0b11
    g2 = (gC >> 6) & 0b11
    b2 = (bC >> 6) & 0b11

    w, h = img.size
    new_img = Image.new("RGB", (w, h))

    for y in range(h):
        for x in range(w):
            r, g, b = img.getpixel((x, y)) #type: ignore

            # clear last 2 bits, insert new value
            r = (r & 0b11111100) | r2
            g = (g & 0b11111100) | g2
            b = (b & 0b11111100) | b2

            new_img.putpixel((x, y), (r, g, b))

    new_img.save(outfile)
apply_color_bits("C:/Users/Sahil/Desktop/InfoSec/image.png", (200, 120, 50), "C:/Users/Sahil/Desktop/InfoSec/output.png")