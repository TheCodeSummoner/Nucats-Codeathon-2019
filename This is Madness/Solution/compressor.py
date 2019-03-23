from random import randint
from zipfile import ZipFile
from os import remove, path


def next_zip(file_path: str) -> str:
    """
    This function is used to zip the given file.

    :param file_path: Path to the file to zip
    :return: Path to the new file
    """

    # Create a new, random name of the zip file
    name = path.join("..", str(randint(10000, 99999)) + ".zip")

    # Zip given file under the new name
    with ZipFile(name, mode="w") as zf:
        zf.write(file_path)

    # Return the file name to use later
    return name


def zip_recursively(file_path: str, depth: int):
    """
    This function is used to zip a file multiple times.

    :param file_path: Path to the file to zip
    :param depth: Number of zip layers
    """

    # Initialise the current zip name
    current = next_zip(file_path)

    # Iterate over the zip depth
    for i in range(depth):

        # Remember current file_path to remove the file later
        temp = current

        # Create a new zip layer
        current = next_zip(current)

        # Remove the previous file
        remove(temp)


if __name__ == '__main__':

    # Zip the challenge text file into multiple layers
    zip_recursively(path.join("..", "recursive_madness_level_2.txt"), 100)
