def to_bits(s):
    return ''.join(f"{ord(c):08b}" for c in s)

def from_bits(bits):
    return ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def encode(cover_file, secret_file, output_file):
    cover_lines = open(cover_file).read().splitlines()
    secret_msg = open(secret_file).read()
    bits = to_bits(secret_msg)

    if len(bits) > len(cover_lines):
        raise ValueError("Not enough lines in cover text")

    encoded = []
    for i, line in enumerate(cover_lines):
        if i < len(bits):
            if bits[i] == "0":
                encoded.append(line + " ")     # space → 0
            else:
                encoded.append(line + "\t")    # tab → 1
        else:
            encoded.append(line)

    open(output_file, "w").write("\n".join(encoded))
    print("Message hidden in", output_file)

def decode(stego_file):
    bits = ""
    for line in open(stego_file).read().splitlines():
        if line.endswith(" "):
            bits += "0"
        elif line.endswith("\t"):
            bits += "1"
    return from_bits(bits)

# --------------------------
# Example usage
# --------------------------
encode("cover_text.txt", "secret_message.txt", "stego_output.txt")
print("Recovered message:", decode("stego_output.txt"))
