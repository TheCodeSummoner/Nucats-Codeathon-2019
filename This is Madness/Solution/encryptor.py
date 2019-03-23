from binascii import b2a_base64 as b64
from os import path


def next_bin(text: str) -> str:
    """
    This function is used to convert given string to binary string.

    :param text: Text to be converted to binary
    :return: String representation of the binary text
    """

    # Convert given text to the binary format
    text = bin(int.from_bytes(bytes(text, encoding="ascii"), "big"))[2:]

    # Add leading zero-s
    text = "0"*(8 - len(text) % 8) + text

    # Return the binary text
    return text


def next_b64(text: str) -> str:
    """
    This function is used to convert given string to base64 string.

    :param text: Text to be converted to base64
    :return: String representation of the base64 text
    """

    # Convert the given text to the base64 format
    text = b64(bytes(text, encoding="ascii"))

    # Return stripped text as a string
    return str(text.strip(), encoding="ascii")


def encrypt_recursively(message: str, steps: int) -> str:
    """
    Function to encrypt (or rather, encode) a message multiple times.

    :param message: Message to be encoded
    :param steps: Number of encoding steps
    :return: Encrypted message
    """

    # Iterate over the steps
    for i in range(steps):

        # Covert current message to binary
        message = next_bin(message)

        # Convert current message to base64
        message = next_b64(message)

    # Return the final message
    return message


if __name__ == "__main__":

    # Create the flag message
    flag = "THIS! IS! FLAG! Actually, the flag is where the battle took place"

    # Open the flag file location
    with open(path.join("..", "recursive_madness_level_2.txt"), "w") as f:

        # Write the encrypted message to the file
        f.write(encrypt_recursively(flag, 6))
