from zipfile import ZipFile
from os import path, remove


def unzip_recursively(file_path):
    """
    This function is used to recursively unzip a multi-layered zip file.

    :param file_path: Path to the file to unzip
    """

    # Initialise the name
    name = ".zip"

    # Keep extracting while there are files to extract
    while ".zip" in name:

        # Open the zip to extract from
        with ZipFile(file_path, mode="r") as zf:

            # Fetch the name of the file inside
            new_name = zf.namelist()[0]

            # Extract the file
            zf.extractall(path.dirname(__file__))

            # Close the ZipFile instance to let os operate on the file
            zf.close()

            # Remove the previous file
            try:
                remove(name)
            except FileNotFoundError:
                pass

            # Override the name to handle the next file
            name, file_path = new_name, new_name


if __name__ == '__main__':

    # Unzip the file recursively
    unzip_recursively(path.join("..", "58869.zip"))
