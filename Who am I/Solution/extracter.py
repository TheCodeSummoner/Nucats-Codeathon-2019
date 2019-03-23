import cv2
import numpy as np
from PIL import Image
from os import path


def extract_original(file_path: str):
    """
    This function is used to show the hidden file in the given image.

    :param file_path: Path to the file to extract hidden information from
    """

    # Initialise a new list of final pixels
    final_pixels = []

    # Extract the pixel values
    for pixels in Image.open(file_path).getdata():
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

    # Show the solution to the challenge
    extract_original(path.join("..", "who_am_i.png"))