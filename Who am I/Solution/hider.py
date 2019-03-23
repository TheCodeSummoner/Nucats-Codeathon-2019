import cv2
from PIL import Image
from os import remove, path
import numpy as np


def convert_to_black_white(filename: str, path: str):

    # Read the image
    img = cv2.imread(filename)

    # Threshold the image
    thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Save the image
    cv2.imwrite(path, thresh)


def convert_to_binary(filename: str) -> str:

    # Convert the picture to black and white
    convert_to_black_white(filename, "temp.png")

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


def hide_bits(path:str, binary: str):

    # Create a new image of expected size
    img = Image.new("RGBA", (128, 128))

    # Load pixel map
    pixels = img.load()

    # Iterate over the map and set each pixel to create a gradient
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = (i, j, 100, 255 - int(binary[i*128 + j]))

    # Save the image
    img.save(path)


def extract_original(filename: str):

    # Initialise a new list of final pixels
    final_pixels = []

    # Extract the pixel values
    for pixels in Image.open(filename).getdata():
        if pixels[3] == 255:
            final_pixels.append(0)
        else:
            final_pixels.append(255)

    # Create a new, blank picture
    img = np.zeros((128, 128, 3), np.uint8)

    # Populate the image with pixels
    for y in range(len(img)):
        for x in range(len(img)):
            img[x, y] = final_pixels[128*y + x]

    # Show the extracted image
    cv2.imshow('extracted', img)
    cv2.waitKey(0)


if __name__ == '__main__':

    img_path = path.join("..", "who_am_i.png")

    hide_bits(img_path, convert_to_binary("pikachu.png"))
    extract_original(img_path)