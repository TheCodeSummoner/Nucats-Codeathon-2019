def decrypt(encrypted: str, side: int) -> str:
    """
    This function is used to decrypt a Caeasar Box encrypted message.

    :param encrypted: Encrypted message
    :param side: Size of the box (side of the square)
    :return: Decrypted message
    """

    # Decrypt the string by using the standard decryption approach (read columns)
    return "".join("".join(char for char in encrypted[i::side]) for i in range(side))


if __name__ == '__main__':

    # Print the decrypted string for this challenge
    print(decrypt("IICEMCSORFAANELMWQDAEIUIG", 5))
