from random import randint
from zipfile import ZipFile
from os import remove


def next_zip(filename: str) -> str:

    # Create a new, random name
    name = str(randint(10000, 99999)) + ".zip"

    # Open a new zip file and write to it
    with ZipFile(name, mode="w") as zf:
        zf.write(filename)

    # Return the file name to use later
    return name


def zip_recursively(filename: str, depth: int):

    # Initialise the current zip name
    current = next_zip(filename)

    # Iterate over the zip depth
    for i in range(depth):

        # Remember current filename to remove the file laterr
        temp = current

        # Create a new zip layer
        current = next_zip(current)

        # Remove the previous file
        remove(temp)


if __name__ == '__main__':
    zip_recursively("recursive_madness_level_2.txt", 100)
