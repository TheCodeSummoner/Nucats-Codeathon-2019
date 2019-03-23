import cv2
from PIL import Image
from os import remove, path


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


if __name__ == '__main__':
    img_path = path.join("..", "who_am_i.png")
    hide_bits(img_path, convert_to_binary("pikachu.png"))
