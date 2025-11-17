from PIL import Image

def embed_image(cover_path, secret_path, outfile):
    cover = Image.open(cover_path).convert("RGB")
    secret = Image.open(secret_path).convert("RGB")

    w, h = secret.size
    if w > cover.size[0] or h > cover.size[1]:
        raise ValueError("Secret image must be smaller")

    cover_px = cover.load()
    secret_px = secret.load()

    for y in range(h):
        for x in range(w):
            cr, cg, cb = cover_px[x, y] #type: ignore
            sr, sg, sb = secret_px[x, y] #type: ignore

            cr = (cr & 0b11111100) | (sr >> 6)
            cg = (cg & 0b11111100) | (sg >> 6)
            cb = (cb & 0b11111100) | (sb >> 6)

            cover_px[x, y] = (cr, cg, cb) #type: ignore

    cover.save(outfile)

def extract_image(stego_path, w, h, outfile):
    stego = Image.open(stego_path).convert("RGB")
    px = stego.load()
    new_img = Image.new("RGB", (w, h))

    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y] #type: ignore
            sr = (r & 0b11) << 6
            sg = (g & 0b11) << 6
            sb = (b & 0b11) << 6
            new_img.putpixel((x, y), (sr, sg, sb))

    new_img.save(outfile)

if __name__ == "__main__":
    embed_image("cover.png", "secret.png", "stego.png")
    extract_image("stego.png", 100, 100, "extracted.png")
