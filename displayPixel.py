from PIL import Image

def extract_colors(path):
    img = Image.open(path).convert("RGB")
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))  # type: ignore
            print(f"Pixel ({x},{y}) : R={r}, G={g}, B={b}")

def modify_bits(rgb, bitmask):
    r, g, b = rgb
    return (r ^ bitmask, g ^ bitmask, b ^ bitmask)

# extract_colors("C:/Users/Sahil/Desktop/InfoSec/image.png")
print(modify_bits((200,100,150),3))