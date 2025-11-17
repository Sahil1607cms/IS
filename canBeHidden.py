from PIL import Image

def CanbeHidden(cover_path, secret_path):
    cover = Image.open(cover_path)
    secret = Image.open(secret_path)

    if secret.size[0] <= cover.size[0] and secret.size[1] <= cover.size[1]:
        return "Yes"
    return "No"
