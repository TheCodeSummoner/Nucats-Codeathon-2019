from binascii import b2a_base64 as b64


def next_bin(text: str) -> str:

    # Convert the given text to the binary format
    text = bin(int.from_bytes(bytes(text, encoding="ascii"), "big"))[2:]

    # Add leading zero-s
    text = "0"*(8 - len(text) % 8) + text

    # Return the encrypted text
    return text


def next_b64(text: str) -> str:

    # Convert the given text to the base64 format
    text = b64(bytes(text, encoding="ascii"))

    # Return stripped text as string
    return str(text.strip(), encoding="ascii")


def encrypt_recursively(message: str, steps: int) -> str:

    # Iterate over the steps
    for i in range(steps):
        print(i)
        # Covert current message to binary
        message = next_bin(message)

        # Convert current message to base64
        message = next_b64(message)

    # Return the final message
    return message


if __name__ == "__main__":

    flag = "THIS! IS! FLAG! Actually, the flag is where the battle took place"

    with open("recursive_madness_level_2.txt", "w") as f:
        f.write(encrypt_recursively(flag, 6))
