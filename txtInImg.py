from PIL import Image
from typing import Any

def message_to_codes(msg):
    msg = msg.upper()
    codes = []
    for ch in msg:
        if ch == " ":
            codes.append(27)
        else:
            codes.append(ord(ch) - 64)
    codes.append(0)
    return codes

def codes_to_chunks(codes):
    chunks = []
    for c in codes:
        b = f"{c:06b}"
        chunks.append((int(b[0:2],2), int(b[2:4],2), int(b[4:6],2)))
    return chunks

def hide_message(image_path, message, out_path):
    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    pixels: Any = img.load()

    codes = message_to_codes(message)
    chunks = codes_to_chunks(codes)

    if len(chunks) > w * h:
        raise ValueError("Message too long for this image")

    index = 0
    for y in range(h):
        for x in range(w):
            if index >= len(chunks):
                break
            a, b, c = chunks[index]
            r, g, b0 = pixels[x, y]
            r = (r & 0b11111100) | a
            g = (g & 0b11111100) | b
            b0 = (b0 & 0b11111100) | c
            pixels[x, y] = (r, g, b0)
            index += 1

    img.save(out_path)

def retrieve_message(stego_path):
    img = Image.open(stego_path).convert("RGB")
    w, h = img.size
    px: Any = img.load()

    codes = []
    code: int = -1
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            a = r & 0b11
            b2 = g & 0b11
            c = b & 0b11
            code = (a << 4) | (b2 << 2) | c
            codes.append(code)
            if code == 0:
                break
        if code == 0:
            break

    message = ""
    for v in codes[:-1]:
        if v == 27:
            message += " "
        else:
            message += chr(v + 64)
    return message


hide_message("C:/Users/Sahil/Desktop/InfoSec/image.png", "hello", "C:/Users/Sahil/Desktop/InfoSec/hello.png")
print(retrieve_message( "C:/Users/Sahil/Desktop/InfoSec/hello.png"))