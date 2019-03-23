from binascii import a2b_base64


def decrypt_recursively(file_path: str) -> str:
    """
    This function is used to decrypt multiple layers of binary, base64 encryptions

    :param file_path: Path to the file to decrypt
    :return: Decrypted string
    """

    # Fetch the encrypted string to decrypt
    with open(file_path) as f:
        encrypted = f.readline()

    # Keep decrypting
    while True:

        try:
            # Decode from base64
            encrypted = str(a2b_base64(encrypted), encoding='ascii')

            # Decode from binary
            encrypted = str(int(encrypted, 2).to_bytes(len(encrypted), 'big'), encoding='ascii')

        # Once value error met, the decryption can not continue
        except ValueError:
            return encrypted


if __name__ == "__main__":

    # Write the encrypted message to the file
    print(decrypt_recursively("recursive_madness_level_2.txt"))
