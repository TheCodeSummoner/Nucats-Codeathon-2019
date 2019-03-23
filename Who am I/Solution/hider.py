import cv2
from PIL import Image
from os import remove, path


def convert_to_black_white(file_path: str, output_path: str):
    """
    This function is used to convert an image to binary-like values (full black/white)

    :param file_path: Path to the file to convert
    :param output_path: Path to the output location
    """

    # Read the image
    img = cv2.imread(file_path)

    # Threshold the image
    thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Save the image
    cv2.imwrite(output_path, thresh)


def convert_to_binary(file_path: str) -> str:
    """
    This function is used to convert a file into a binary string representing it.

    :param file_path: Path to the file to convert
    :return: Binary representation of the file
    """

    # Convert the picture to black and white
    convert_to_black_white(file_path, "temp.png")

    # Initialise the string to return
    binary = ""

    # Iterate over the pixels in the image
    for pixel in Image.open("temp.png").getdata():

        # Add the next binary number
        if not pixel:
            binary += "0"
        else:
            binary += "1"

    # Remove the temporary file
    remove("temp.png")

    # Return the formatted string
    return binary


def hide_bits(file_path: str, binary: str):
    """
    This function is used to hide the binary string representation of an image into a new gradient-like image

    :param file_path: Path to the output location
    :param binary: Binary representation of an image
    """

    # Create a new image of expected size
    img = Image.new("RGBA", (128, 128))

    # Load the pixel map
    pixels = img.load()

    # Iterate over the map and set each pixel to create a gradient
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (i, j, 100, 255 - int(binary[i*128 + j]))

    # Save the image
    img.save(file_path)


if __name__ == '__main__':

    # Hide the original image into a gradient image
    hide_bits(path.join("..", "who_am_i.png"), convert_to_binary("pikachu.png"))
