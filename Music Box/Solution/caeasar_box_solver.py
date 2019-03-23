def decrypt(encrypted: str, side: int) -> str:

    # Initialise the string to build over time
    decrypted = ""

    # Iterate over columns
    for i in range(side):

        # Build up each part of the string
        decrypted += "".join(char for char in encrypted[i::side])

    # Return the decrypted string
    return decrypted


if __name__ == '__main__':
    print(decrypt("IICEMCSORFAANELMWQDAEIUIG", 5))