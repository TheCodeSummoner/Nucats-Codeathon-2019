# Solution

### Description

To obtain the solution, follow the steps:

1. Load *who_am_i.png* into `RGBA`-valued data structure.

2. Notice that the alpha channel always has values `255` or `254`, which correspond to the *binary* format.

3. Extract the alpha channel and build a new image with it, where `255`, `254` map to pixel values `0`, `255`.

4. Find the flag (character in the image) -> *Pikachu*

### Extras

1. *hider.py* was used to hide the image inside a colour gradient.

2. *extracter.py* can be used to extract the hidden image

3. *pikachu.png* is the original image.

http://www.phrack.org/issues/7/3.html

https://www.dcode.fr/book-cipher

Loyd Blankenship

### Author

Kacper Florianski
